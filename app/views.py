from django.shortcuts import render,redirect
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def tutorial(request):
    return render(request,"tutorial.html")


def blog(request):
    return render(request,"blog.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

    # Save to database
        contact = Contact(name = name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
        messages.success(request,"Message Sent")
        return render(request,"contact.html")
    return render(request,"contact.html")

def signin(request):
    return render(request,"signin.html")

def which(request):
    return render(request,"which.html")

def fast(request):
    return render(request,"fast.html")

def study(request):
    return render(request,"study.html")

def supercomputer(request):
    return render(request,"supercomputer.html")

def quantumcomputer(request):
    return render(request,"quantumcomputer.html")

def softwareengineer(request):
    return render(request,"softwareengineer.html")

def webdevloper(request):
    return render(request,"webdevloper.html")

def appdevloper(request):
    return render(request,"appdevloper.html")

def aiengineer(request):
    return render(request,"aiengineer.html")

def py_intro(request):
	return render(request,"py_intro.html")

def py_install(request):
	return render(request,"py_install.html")

def py_syntax(request):
	return render(request,"py_syntax.html")

def py_comment(request):
	return render(request,"py_comments.html")

def py_variable(request):
	return render(request,"py_variable.html")

def py_datatype(request):
	return render(request,"py_datatype.html")
	
def operator(request):
	return render(request,"py_operator.html")

def py_input(request):
	return render(request,"py_input.html")

def type_casting(request):
	return render(request,"type_casting.html")

def py_string(request):
	return render(request,"py_string.html")

def str_method(request):
	return render(request,"str_method.html")
	
def f_string(request):
	return render(request,"f-string.html")

def escape(request):
	return render(request,"escape.html")
	
def py_list(request):
	return render(request,"py_list.html")

def list_index(request):
	return render(request,"list_index.html")

def list_method(request):
	return render(request,"list_method.html")
	
def py_tuple(request):
	return render(request,"py_tuple.html")

def tuple_indexes(request):
	return render(request,"tuple_index.html")
	

def tuple_manipulating(request):
	return render(request,"tuple_manipulating.html")

def py_set(request):
	return render(request,"set.html")

def set_method(request):
	return render(request,"set_method.html")

def py_dict(request):
	return render(request,"py_dict.html")

def dict_access(request):
	return render(request,"dict_access.html")

def add_remove_dict(request):
	return render(request,"add_remove_dict.html")

def py_if(request):
	return render(request,"py_if.html")
	

def py_if_else(request):
	return render(request,"py_if_else.html")

def py_if_else(request):
	return render(request,"py_if_else.html")

def py_if_elif_else(request):
	return render(request,"py_if_elif_else.html")


def py_nested_if(request):
	return render(request,"py_nested_if.html")
	
def py_for_loop(request):
	return render(request,"py_for_loop.html")
	
def py_while_loop(request):
	return render(request,"py_while_loop.html")

def py_break(request):
	return render(request,"py_break.html")

def py_continue(request):
	return render(request,"py_continue.html")
	
def py_function(request):
	return render(request,"py_function.html")

def py_func_arg(request):
	return render(request,"func_arg.html")

def py_module(request):
	return render(request,"py_module.html")

def py_oops(request):
	return render(request,"py_oops.html")
	
def py_self(request):
	return render(request,"py_self.html")
	
def __init__(request):
	return render(request,"__init__.html")
		
def py_error(request):
	return render(request,"py_error.html")
	
def py_project_1(request):
	return render(request,"sps.html")

def py_project_2(request):
	return render(request,"jarvis.html")

def basic_linux(request):
	return render(request,"basic_linux.html")

def linux_basic_command(request):
	return render(request,"linux_basic_command.html")

def file_linux(request):
	return render(request,"file_linux.html")

def network_linux(request):
	return render(request,"network_linux.html")