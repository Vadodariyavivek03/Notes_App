from django.shortcuts import render, redirect
from User_App.models import *
from datetime import datetime 
from django.core.mail import send_mail
from Final_Project import settings
from django.contrib import messages
from User_App.forms import *
from django.db.models import Q
from User_App.views import notes


# Create your views here.

def admin_login(request):

    if request.method == "POST":
        unm = request.POST['username'].strip()
        pwd = request.POST['password'].strip()
        
        if unm and pwd:
            if unm == 'admin' and pwd == 'admin@123':
                print(" Admin Login Successful..!! ")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid username or password. Please try again...!!")

    return render(request, 'admin_login.html')

# ----------------------------------------------------------------------------------------- #

def admin_dashboard(request):
    search_query = request.GET.get('search')

    recent_users = UserSignup.objects.order_by('-id')

    total_users = UserSignup.objects.count()
    total_notes = mynotes.objects.count()
    total_inquiry = contact.objects.count()
    pending_status = mynotes.objects.filter(status='pending').count()

    if search_query:
        recent_users = recent_users.filter(
            Q(fullname__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(mobile__icontains=search_query)
        )

    recent_users = recent_users[:5]
    
    context = {
        'recent_users': recent_users,
        'total_users': total_users,
        'total_notes': total_notes,
        'total_inquiry': total_inquiry,
        'pending_status': pending_status,
    }

    return render(request, 'admin_dashboard.html', context)

# ----------------------------------------------------------------------------------------- #

def admin_userdata(request):
    search_query = request.GET.get('search')

    if search_query:
        users = UserSignup.objects.filter(
            Q(fullname__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(mobile__icontains=search_query)
        )
    else:
        users = UserSignup.objects.all()

    return render(request, 'admin_userdata.html', {
        'users': users,
        'search_query': search_query
    })

# ----------------------------------------------------------------------------------------- #

def admin_notesdata(request):
    notesdata=mynotes.objects.all()
    users = UserSignup.objects.all()

    query = request.GET.get("search", "")

    if query:
        notesdata = notesdata.filter(
            Q(user__fullname__icontains=query) |
            Q(title__icontains=query) |
            Q(desc__icontains=query) |
            Q(subject__icontains=query)
        )

    return render(request,'admin_notesdata.html',{'notesdata':notesdata, 'users': users})

# ----------------------------------------------------------------------------------------- #

def admin_logout(request):
    return redirect('admin_login')

# ----------------------------------------------------------------------------------------- #

def notes_approve(request, id):
    note = mynotes.objects.get(id=id)
    note.status = 'Approved'
    note.updated_at = datetime.now()
    note.save()

    # Email notification code
     
    subject = 'Your Note has been Approved'

    mail_msg = f'Dear {note.user.fullname},\n\nYour note titled "{note.title}" has been approved by the admin and is now available on the platform.\n\nThank you for your contribution!\n\nBest regards,\nAdmin Team'

    from_to = 'vivekvadodariya783@gmail.com'

    to_email = settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=mail_msg, from_email=from_to, recipient_list=[to_email])
    
    messages.success(request, f"{note.user.fullname} : This {note.title}_Note Approved and User Notified via Email..!!")

    return redirect('admin_notesdata')


# ----------------------------------------------------------------------------------------- #

def notes_reject(request, id):
    note = mynotes.objects.get(id=id)
    note.status = 'Rejected'
    note.updated_at = datetime.now()
    note.save()

    # Email notification code

    subject = 'Your Note has been Rejected'
   
    mail_msg = f'Dear {note.user.fullname},\n\nWe regret to inform you that your note titled "{note.title}" has been rejected by the admin.\n\nPlease review our submission guidelines and consider making necessary changes before resubmitting.\n\nBest regards,\nAdmin Team'
  
    from_to = 'vivekvadodariya783@gmail.com'
   
    to_email = settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=mail_msg, from_email=from_to, recipient_list=[to_email])
    
    messages.success(request, f"{note.user.fullname} : This {note.title}_Note Rejected and User Notified via Email..!!")

    return redirect('admin_notesdata')

# ----------------------------------------------------------------------------------------- #

def admin_settings(request):
    return render(request, 'admin_settings.html')

# ----------------------------------------------------------------------------------------- #

def admin_inquiry(request):
    search_query = request.GET.get('search')

    if search_query:
        inquiry = contact.objects.filter(
            Q(fullname__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(msg__icontains=search_query) 
        )
    else:
        inquiry = contact.objects.all()

    return render(request, 'admin_inquiry.html', {
        'inquiry': inquiry,
        'search_query': search_query
    })

# ----------------------------------------------------------------------------------------- #

def update_userdata(request, id):
    user_data = UserSignup.objects.get(id=id)

    if request.method == "POST":
        user_data.fullname = request.POST['fullname']
        user_data.email = request.POST['email']
        user_data.mobile = request.POST['mobile']
        user_data.save()

        messages.success(request, f"{user_data.fullname} : Profile Data Updated Successfully...!!")

        return redirect('admin_userdata')

    return redirect('admin_userdata')

# ----------------------------------------------------------------------------------------- #

def delete_userdata(request, id):
    user_data = UserSignup.objects.get(id=id)
    user_data.delete()

    messages.success(request, f"{user_data.fullname} : Profile Data Deleted Successfully...!!")

    return redirect('admin_userdata')

# ----------------------------------------------------------------------------------------- #

def upload_notes(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = UserSignup.objects.get(id=user_id)

        mynotes.objects.create(
            user=user,
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            subject=request.POST.get("subject"),
            notes_file=request.FILES["notes_file"]
        )

        messages.success(request, f"{user.fullname} : Notes Uploaded Successfully...!!")

        return redirect("admin_notesdata")
    
# ----------------------------------------------------------------------------------------- #

def update_notes_file(request):
    if request.method == "POST":
        note_id = request.POST.get("note_id")

        if not note_id:
            return redirect('admin_notesdata')

        note = mynotes.objects.get(id=note_id)

        if 'notes_file' in request.FILES:
            note.notes_file = request.FILES['notes_file']
            note.save()

        messages.success(request, f"{note.user.fullname}'s Notes File Updated Successfully..!!")

        return redirect('admin_notesdata')
    
# ----------------------------------------------------------------------------------------- #
  
    




