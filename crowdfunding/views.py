from django.shortcuts import render,redirect 
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages,admin
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Project, Fund
from django.utils import timezone

# Create your views here.
from .forms import CreateUserForm


def home(request): #Renders 'crowdfunding/home.html'template 
    return render(request,'crowdfunding/home.html')

def loginpage(request): #Renders 'crowdfunding/login.html'template 
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
             login(request, user)
             return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')
            

    context = {}
    return render(request,'crowdfunding/login.html',context)

def logoutUser(request):  #logout view, sending user back to login page
    logout(request)
    return redirect('loginpage')


def register(request): #Renders 'crowdfunding/register.html'template
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect ('crowdfunding/login.html')

    context = {'form':form}
    return render(request,'crowdfunding/register.html',context)




# query for search, now only search name, need to add more 

def result (request):

        # get search string sent from form
        search_string = request.GET.get('name','')
        #query 
        query = 'SELECT * FROM project WHERE name ~\'%s\' OR category ~\'%s\' or description ~\'%s\' '% (search_string, search_string,search_string) 
        # the connection object
        c = connection.cursor()
        c.execute(query)
        #feth all the rows.fetchall() returns a list of tuples 
        results = c.fetchall()
        result_dict ={'records':results}
        return render(request,'crowdfunding/result.html',result_dict)




#query for all avaialbe project 

def allproject(request):

        query = """SELECT * FROM project WHERE end_date >= now() """
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        result_dict = {'records':result}
        return render(request,'crowdfunding/home.html',result_dict)




# display project currently getting funeded : current_amount >= 0.3*goal 0 or null

def popular(request): 
        query = """select * 
                        from project p, fund f, auth_user a
                        where p.id = f.p_id
                        and a.id = f.u_id
                        AND 0.5*p.goal <=(SELECT SUM(amount)FROM fund f1 
                                        WHERE f1.p_id = p.id
                                        AND f1.u_id = a.id
                                        GROUP BY f1.p_id
                                        ORDER BY SUM(amount))""" 
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        result_dict = {'records':result}


        return render(request,'crowdfunding/popular.html',result_dict)



# display all the success project where current_amount >= goal 

def success(request): 

        query = """select * 
                        from project p, fund f, auth_user a
                        where p.id = f.p_id
                        and a.id = f.u_id
                        AND p.goal <=(SELECT SUM(amount)FROM fund f1 
                                        WHERE f1.p_id = p.id
                                        AND f1.u_id = a.id
                                        GROUP BY f1.p_id)""" 
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        result_dict = {'records':result}
        return render(request,'crowdfunding/success.html',result_dict)

# create project as a user
@login_required(login_url='loginpage') #send user back to login page if not login

def create(request):
        if request.method == "POST":
                projectname = request.POST["projectname"]
                description = request.POST ["description"]
                category = request.POST["category"]
                location = request.POST["location"]
                startdate = request.POST["startdate"]
                enddate = request.POST["enddate"]
                goal = request.POST["goal"]
                username = request.user
                #newproject = Project(name=projectname,description = description, location= location,category =category,start_date=startdate,end_date=enddate,username= username,goal=goal,status = "started")
                #newproject.save()

                query = """INSERT INTO project (name, description,location,category,start_date,end_date,username,goal) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\') """ % (projectname,description,location,category,startdate,enddate,username,goal)

                c = connection.cursor()
                c.execute(query)

                return redirect('home')


                
                
        return render(request, "crowdfunding/createproject.html")




# individual project details page
@login_required(login_url='loginpage')
def detail(request,project):
        query = "SELECT * FROM project WHERE id = \'%s\'"% (project)
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        project_dict = {'record':result}
        
        
        if request.method == "POST":
                project = request.POST["projectid"]
                userid = request.user.pk
                fund = request.POST ["amount"]
                #print(userid)
                #newfund = Fund()
                #newfund.p_id = project
                #newfund.u_id = userid
                #newfund.amount = fund
                messages.success(request, 'Thank you for supporting!')


                #newfund = Fund(p_id = project, u_id = userid, amount = fund)   this is updating
                #newfund.save()
                query = """Insert into fund (p_id,u_id, amount) values (\'%s\',\'%s\',\'%s\') """ % (project,userid,fund)
                c = connection.cursor()
                c.execute(query)

                #updating total amount for the user
                query = """UPDATE auth_user SET projects_supported = (
                                                        SELECT  COUNT(f.u_id) 
                                                        FROM fund f, auth_user a
                                                        where f.u_id = a.id AND a.id = %s
                                                        GROUP BY (f.u_id)) WHERE id = \'%s\'""" % (userid,userid)

                c = connection.cursor()
                c.execute(query)

                #update the total amount also 

                query = """UPDATE auth_user SET total_amount = (
                                                        SELECT  SUM(f.amount) 
                                                        FROM fund f, auth_user a
                                                        where f.u_id = a.id AND a.id = %s
                                                        GROUP BY (f.u_id)) WHERE id = \'%s\'""" % (userid,userid)
                c = connection.cursor()
                c.execute(query)

                # change the status of the project to finished if exceed goal
                query = """UPDATE project SET status = 'finished' WHERE project.goal <= (SELECT SUM(f.amount)
                                                                                                FROM fund f, project p
                                                                                                WHERE f.p_id = p.id AND p.id = %s)""" % (project)
                c = connection.cursor()
                c.execute(query)

                return redirect('home')


        
        return render(request, "crowdfunding/detail.html",project_dict)
# individual project details page
#def detail(request,project):
#        detail = Project.objects.get(pk=project)
#
 #       return render(request, "crowdfunding/detail.html")
