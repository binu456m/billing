from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
import json
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from cheques.forms import ChequeForm
from cheques.models import Cheque
from app.functions import get_current_shop, generate_form_errors
from django.contrib.auth.decorators import login_required
from app.decorators import check_group
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
@check_group(['admin'])
def create_cheque(request):
    if request.method == "POST":
        form = ChequeForm(request.POST)
            
        if form.is_valid():

            #get current shop
            shop = get_current_shop(request) 

            #create cheque
            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.shop = shop
            data.save()
            
            request.session['message'] = 'Form Submitted successfully'
            return HttpResponseRedirect(reverse('cheques:view_cheque', kwargs = {'pk' : data.pk}))
        
        else:    
            errors =generate_form_errors(form,formset=False)   
            context = {
	            "form" : form,
	            "title" : "Error",
                "errors":errors,
                "cheques_active":"active"
	            
	        }          
            
        return render(request, 'cheques/entry_cheque.html', context)

    else: 
        form = ChequeForm()
        
        context = {
            "form" : form,
            "title" : "Create Cheque",
            "url" : reverse('cheques:create_cheque'),
            "redirect" : True,
            "cheques_active":"active"
            
        }
        return render(request, 'cheques/entry_cheque.html', context)
    
    
@login_required
@check_group(['admin'])
def edit_cheque(request,pk):
    instance = get_object_or_404(Cheque.objects.filter(pk=pk,is_deleted=False))
    
    if request.method == "POST":
        response_data = {}  
        form = ChequeForm(request.POST,instance=instance)
        
        if form.is_valid(): 
            
            #update cheque
            data = form.save(commit=False)
            data.updater = request.user
            data.date_updated = datetime.datetime.now()
            data.save()
            
            request.session['message'] = 'Form Edited successfully'
            return HttpResponseRedirect(reverse('cheques:view_cheque', kwargs = {'pk' : data.pk}))
        else:
            errors =generate_form_errors(form,formset=False)
            context = {
                "form" : form,
                "title" : "Update Cheque",
                "cheques_active":"active"
            }          
            
        return render(request, 'cheques/entry_cheque.html', context)

    else: 
        form = ChequeForm(instance=instance)
        
        context = {
            "form" : form,
            "title" : "Edit cheque : " + instance.name,
            "instance" : instance,
            "cheques_active":"active"
        }
        return render(request, 'cheques/entry_cheque.html', context)

       
@login_required
@check_group(['admin'])
def view_cheques(request):
    current_shop = get_current_shop(request)
    instances = Cheque.objects.filter(shop=current_shop,is_deleted=False)

    try:
        message = request.session['message']
        del request.session['message']
    except KeyError:
        message = None

    title = "Cheques"


    #filter by query
    query = request.GET.get("q")
    if query:
        title = "Cheques (%s)" % query
        try:
            date_query = datetime.datetime.strptime(query,"%d-%m-%y")
        except:
            date_query = query
        instances = instances.filter(Q(name__icontains=query)|Q(date__icontains=date_query))

    #code for page nation starts here
    paginator = Paginator(instances, 100)
    page = request.GET.get('page')

    try:
        instances = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        instances = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        instances = paginator.page(paginator.num_pages)
        
    context = {
        'title' : title,
        "instances" : instances,
        'query':query,
        "message" : message,
        "cheques_active":"active" 
    }
    return render(request,'cheques/view_cheques.html',context) 


@login_required
@check_group(['admin'])
def view_cheque(request,pk):
    instance = get_object_or_404(Cheque.objects.filter(pk=pk,is_deleted=False))
    
    try:
        message = request.session['message']
        del request.session['message']
    except KeyError:
        message = None

    context = {
        "instance" : instance,
        "title" : "Cheque : " + str(instance.name),
        "message" : message,
        "cheques_active":"active"
    }
    return render(request,'cheques/view_cheque.html',context)


@login_required
@check_group(['admin'])
def delete_cheque(request,pk):
    instance = get_object_or_404(Cheque.objects.filter(pk=pk))
    Cheque.objects.filter(pk=pk).update(is_deleted=True)
    
    request.session['message'] = 'Successfully Deleted'
    return HttpResponseRedirect(reverse('cheques:view_cheques'))


@login_required
@check_group(['admin'])
def create_cheque_popup(request): 

    if request.method == "POST":
        #get current shop
        shop = get_current_shop(request) 
        form = ChequeForm(request.POST,request=request)
            
        if form.is_valid():

            #create cheque_id
            cheque_id = 1
            cheque_obj = Cheque.objects.filter(shop=shop).order_by("-date_added")[:1]
            if cheque_obj:
                for cheque in cheque_obj:
                    cheque_id = cheque.cheque_id + 1
            

            #create farmer
            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.cheque_id = cheque_id
            data.shop = shop
            data.save()
            
            response_data ={
                'status':'true',
                'message': "Cheque %s Created Successfully" %(data.name),
            }
            
            response = HttpResponse(json.dumps(response_data), content_type='application/javascript')
            return response
        
        else:    
            errors =generate_form_errors(form,formset=False)   
            response_data = {
                'status':'false',
                'message': errors,
            }
            response = HttpResponse(json.dumps(response_data), content_type='application/javascript')  
            return response