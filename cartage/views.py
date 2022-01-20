from django.shortcuts import render, get_object_or_404

from django.db.models import Q
# Create your views here.
from django.utils import timezone

from cartage.models import User, Address, Trip, Contact, Message


def index(request):
    try:
        user = User.objects.filter(pk=request.session['user_id'])
    except(KeyError):
        return render(request, 'cartage/index.html')
    return render(request, 'cartage/index.html', {'user' : user})


def login(request):
    return render(request, 'cartage/login.html')


def landingL(request):
    user = get_object_or_404(User, pk=User.objects.get(email=request.POST['email']).id)
    if user.password == request.POST['password']:
        request.session['user_id'] = user.id
        return render(request, 'cartage/index.html', {'type': "Connexion réussie !", 'user': user})
    else:
        return render(request, 'cartage/login.html')


def landingR(request):
    if User.objects.filter(email=request.POST['email'], tel=request.POST['tel']).count() == 0:
        st = " ".join(request.POST['street'].split())
        zi = " ".join(request.POST['zip_code'].split())
        ci = " ".join(request.POST['city'].split())
        if Address.objects.filter(street=st, zip_code=zi, city=ci).count() == 0:
            a = Address(street=st,
                        zip_code=zi,
                        city=ci)
            a.save()
        else:
            a = Address.objects.get(street=st, zip_code=zi, city=ci)
        user = User(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            address=a,
            email=request.POST['email'],
            password=request.POST['password'],
            tel=request.POST['tel'],
            car=request.POST['car'],
            rating=0,
            total_votes=0,
            hours=request.POST['hours']
        )
        user.save()
        request.session['user_id'] = user.id
        return render(request, 'cartage/index.html', {'type': "Inscription réussie !", 'user': user})
    else:
        return render(request, 'cartage/register.html')


def register(request):
    return render(request, 'cartage/register.html')


def trips(request):
    if request.POST:
        user1 = User.objects.get(pk=request.session['user_id']) if request.POST['madeByTeacher'] else None
        user2 = None if request.POST['madeByTeacher'] else User.objects.get(pk=request.session['user_id'])
        start_st = " ".join(request.POST['start_street'].split())
        start_zi = " ".join(request.POST['start_zip'].split())
        start_ci = " ".join(request.POST['start_city'].split())

        stop_st = " ".join(request.POST['stop_street'].split())
        stop_zi = " ".join(request.POST['stop_zip'].split())
        stop_ci = " ".join(request.POST['stop_city'].split())

        if Address.objects.filter(street=start_st, zip_code=start_zi, city=start_ci).count() == 0:
            start_ad = Address(street=start_st,
                               zip_code=start_zi,
                               city=start_ci)
            start_ad.save()
        else:
            start_ad = Address.objects.get(street=start_st, zip_code=start_zi, city=start_ci)

        if Address.objects.filter(street=stop_st, zip_code=stop_zi, city=stop_ci).count() == 0:
            stop_ad = Address(street=stop_st,
                              zip_code=stop_zi,
                              city=stop_ci)
            stop_ad.save()
        else:
            stop_ad = Address.objects.get(street=stop_st, zip_code=stop_zi, city=stop_ci)

        trip = Trip(
            student=user2,
            teacher=user1,
            start=start_ad,
            stop=stop_ad,
            departure=request.POST['departure']
        )
        trip.save()
    user = User.objects.get(pk=request.session['user_id'])
    user_trips = Trip.objects.filter(Q(teacher_id=user.id) | Q(student_id=user.id))
    return render(request, 'cartage/trips.html', {'trips':user_trips, 'user' : user})


def profile(request):
    user = User.objects.get(pk=request.session['user_id'])
    if request.POST:
        for key in request.POST.keys():
            if key == 'firstname':
                user.firstname = request.POST['firstname']
            elif key == 'lastname':
                user.lastname = request.POST['lastname']
            elif key == 'street':
                st = " ".join(request.POST['street'].split())
                zi = " ".join(request.POST['zip_code'].split())
                ci = " ".join(request.POST['city'].split())
                if Address.objects.filter(street=st, zip_code=zi, city=ci).count() == 0:
                    a = Address(street=st,
                                zip_code=zi,
                                city=ci)
                    a.save()
                else:
                    a = Address.objects.get(street=st, zip_code=zi, city=ci)
                user.address = a
            elif key == 'email':
                if User.objects.filter(email=request.POST['email']).count() == 0:
                    user.email = request.POST['email']
            elif key == 'password':
                if user.password == request.POST['current_password']:
                    user.password = request.POST['password']
            elif key == 'tel':
                if User.objects.filter(tel=request.POST['tel']).count() == 0:
                    user.tel = request.POST['tel']
            elif key == 'car':
                user.car = request.POST['car']
            elif key == 'hours':
                user.hours = request.POST['hours']

        user.save()
    return render(request, 'cartage/profile.html', {'user' : user})


def search(request):
    user = User.objects.get(pk=request.session['user_id'])
    matches = User.objects.filter(car=not user.car)
    return render(request, 'cartage/search.html', { 'matches' : matches})


def messages(request):
    user = User.objects.get(pk=request.session['user_id'])
    if request.POST:
        for key in request.POST.keys():
            if key == 'match':
                if Contact.objects.filter(Q(owner=user, contact = User.objects.get(pk=request.POST['match'])) | Q(owner=User.objects.get(pk=request.POST['match']), contact = user)).count() == 0:
                    contact = Contact(
                        owner=user,
                        contact=User.objects.get(pk=request.POST['match'])
                    )
                    contact.save()
            if key == 'message':
                message = Message(
                    content=request.POST['message'],
                    sender=user,
                    date=timezone.now(),
                    receiver=User.objects.get(pk=request.POST['target'])
                )
                message.save()
    try:
        contacts = Contact.objects.filter(Q(owner=user) | Q(contact=user))
        users_and_messages= []
        for contact in contacts:
            subtab = []

            if contact.owner == user:
                subtab.append(contact.contact)
                if Message.objects.filter(Q(sender=user.id, receiver=contact.contact) | Q(receiver=user.id, sender=contact.contact)).count != 0:
                    subtab.append(Message.objects
                                  .filter(Q(sender=user, receiver=contact.contact) | Q(sender=contact.contact, receiver=user))
                                  .values('content', 'date', 'sender').order_by('date'))
                else:
                    subtab.append([])
            else:
                subtab.append(contact.owner)
                if Message.objects.filter(Q(sender=user.id, receiver=contact.owner) | Q(receiver=user.id, sender=contact.owner)).count != 0:
                    subtab.append(Message.objects
                                  .filter(Q(sender=user, receiver=contact.owner) | Q(sender=contact.owner, receiver=user))
                                  .values('content', 'date', 'sender').order_by('date'))
                else:
                    subtab.append([])
            users_and_messages.append(subtab)

    except(KeyError, Contact.DoesNotExist):
        return render(request, "cartage/search.html")
    finally:
        return render(request,
                      "cartage/messages.html",
                      {'users_and_messages' : users_and_messages,
                       'user' : user,
                       })


def help(request):
    return render(request, 'cartage/help.html')