# SEI Project-03

## Goal

>To develop a full-stack application in Python using the Django framework.

## Team Members

>- Ashish Singh
>- Rob Sesemann
>- Ellie Eadington

## Timeframe

>8 days

## Technologies Used

>- Python
>- Django
>- PgAdmin
>- HTML
>- DTL
>- CSS

## fitCoffee

<img src="main_app\static\uploads\fitcoffee.PNG"/>

>This was my third project for this Software Engineering Immersive course; to build a full-stack Python application built with a team of 3. fitCoffee is an app for coffee enthusiasts, where you can discover cafes that serve your favourite coffee beans, and promote your cafe as a business owner.

Deployed version: https://fitcoffee.herokuapp.com/

## Getting Started/Code Installation

>- Clone the repo
>- Run ‘pip install -r requirements.txt’ to install all of the python modules
>- Run the application using  ‘python manage.py runserver’.

## Planning

### Ideation stage

>First, we brainstormed our app ideas as a team. I was open-minded about the type of project we were going to create, and we quickly settled on an idea from Rob to create an application for coffee lovers. Dissimilar to a regular app to find restaurants and cafes, this app would provide those in search of their perfect cafe the ability to find one by the coffee bean variety they loved the most. I was happy with this idea, as I felt there was the opportunity to implement some interesting features, such as search, filtering and sorting functionalities, as well as an interactive cafe map and functionalities for the two types of user; the general user and the cafe owner.

### Feature planning and allocation

>Once we were happy with our idea, I created a project planning spreadsheet, where we brainstormed the details of the features we wanted to implement, the user stories and a table, breaking down the features further. I wanted the team to work on functionalities that they found interesting, so I took a step back and allowed the other team members to allocate themselves to a desired feature before choosing my own. I then assigned each of us to tasks in the table.

### ERD

<img src="main_app\static\uploads\erd-fitcoffee.PNG"/>

### Wireframes

>Rob did an excellent job at creating the wireframes for the core pages in our site. Once these had been designed, I then went in and added the additional pages that represented the individual views.
<img src="main_app\static\uploads\wireframe-fitcoffee.PNG"/>


### Trello

Next, Rob created a Trello board, where we each populated it with tasks that we were assigning to ourselves. Once we had a solid idea of exactly which tasks we would each be working on, we then decided which tasks we would each work on first, ensuring that this made logical sense, and kept in communication over zoom and our slack channel to ensure that we were able to provide real-time updates to each other.
<img src="main_app\static\uploads\trelloe.PNG"/>

### Build/Code Process

### Set-up

>After creating my Django project, I created the Django app using the startapp command and added it into the installed apps in the settings.py file. Next I installed psycopg2-binary, created our database in pgAdmin and updated the database configurations in settings.py. Next I migrated the django.contrib applications to the database to create their schemas. I then added a urls.py file to my app and then registered it in my project urls.py url patterns. In the newly created file I added in the basic configurations and then defined the url paths for our root, about and home routes. I created the view functions for root, home & about in views.py to generate a basic HttpResponse. I then created a templates folder which included a base.html template for template inheritance across other pages as well as the home & about.html, which I created with Materialize and replaced my HttpResponse with the method to render the correct templates with the request parameter. Once working, I then created a static folder and subfolders for css, uploads and js, and added some basic css in a css file which I linked to the base.html file.

>Next I created the models in models.py according to our ERD diagrams before migrating the models to the database (example below).

```py
class CoffeeBean(models.Model):
    name = models.CharField(max_length=250)
    variety =  models.CharField(max_length=1000, choices=VARIETIES, default=VARIETIES[0][0])
    description = models.CharField(max_length=2000)
    roastery = models.CharField(max_length=250)
    date_harvested = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    location = models.CharField(max_length=250)
```

### Coffee Index, Detail Pages & CRUD Operations

>Whilst Ashish began working on user sign-up and sign-in, Rob and I began working on the cafe and coffee index, detail pages and CRUD operations, respectively. First, I created two functions for my coffee index and detail pages and their corresponding urls and templates, passing the request and request and coffee_bean_id as parameters, respectively. For the detail page, I wanted to display the cafes that served the coffee bean as an additional feature, so I filtered the Cafe objects where there was a match on the joining cafe_coffeebean table.

```py
def coffee_beans_detail(request, coffee_beans_id):
  coffee_bean = CoffeeBean.objects.get(id = coffee_beans_id)
  cafes = Cafe.objects.filter(coffee_beans = coffee_bean)
 
  return render(request, 'coffee_beans/detail.html',{ 'coffee_bean': coffee_bean, 'cafes': cafes})
```

>I then rendered the data in the html files in DTL. I initially struggled to get the images to load, but found a workaround by concatenating the static uploads/ path with the image file name.

```py
{% load static %}
<img src="{% static 'uploads/'%}{{coffee_bean.image}}" alt="coffee_bean_image" width="100" height="100">
```

>Once completed, I moved on to the CUD operations for coffee beans which I was able to test in django admin. First, I created a ModelForm in forms.py and included all of the required fields. When a cafe owner adds a new coffee bean to their menu, the cafe and coffee bean id need to be added to the joining table, and so I first assigned the cafe variable the correct object from the database using the cafe_id from the request which I passed as a query parameter in the url. Then, in my conditional form.is_valid() statement, I saved the form using the save method with the commit parameter assigned to false as I was using a model form that did not include all of the fields that were in the database and did not want the function to throw an error. Once I created a new instance of coffee bean, I initially struggled to update the joining table with the cafe and coffee bean ids. As a workaround, I assigned the coffee bean id an empty array before appending the id to the array. I was then able to populate the table using the set() method.

```py
def add_coffee_bean(request, cafe_id):
    coffee_bean_form = CoffeeBeanForm(request.POST)
    cafe = Cafe.objects.get(id = cafe_id)
    if coffee_bean_form.is_valid():
        new_coffee_bean = coffee_bean_form.save(commit=False)
        new_coffee_bean.cafe_id = cafe_id
        new_coffee_bean.save()
        new_beans_id = []
        new_beans_id.append(new_coffee_bean.pk)
        cafe.coffee_beans.set(new_beans_id)
 
    return redirect('coffee_bean_edit', cafe_id=cafe_id)  
```

>Finally, I created my update and delete CBVs using ModelForms.

### Filtering

>In order to add the filtering functionalities to our coffee and cafe index pages, I used the Django-filter application to add queryset filtering from URL parameters. First I imported django_filters and required models into a new filters.py file, where I defined my filters. In order to provide a dropdown list of choices, I used the ModelChoiceFilter method where I provided the queryset the unique fields from the desired models required for each filter. 
import django_filters as filters
from .models import CoffeeBean, Cafe

```py
class CoffeeBeanFilter(filters.FilterSet):
    roastery = filters.ModelChoiceFilter(field_name = 'roastery', label='Roastery', queryset = CoffeeBean.objects.all().distinct('roastery'))
    class Meta:
        model = CoffeeBean
        fields = ['variety', 'roastery']
 
class CafeFilter(filters.FilterSet):
 
    cafe_name = filters.ModelChoiceFilter(field_name = 'cafe_name', label='Cafe', queryset = Cafe.objects.all().distinct('cafe_name'))
    address_city = filters.ModelChoiceFilter(field_name = 'address_city', label='Location', queryset = Cafe.objects.all().distinct('address_city'))
    class Meta:
        model = Cafe
        fields = ['cafe_name', 'address_city']  
```

>I then imported these filters into views.py to be used to add queryset filtering to the coffee and cafe index views. After defining the data, I defined the filter list by using the imported filter as a method and passing it the request method and queryset data parameters. I then assigned the initial variable the queryset, and passed this and the filter as context parameters to be rendered in the view.

```py
def coffee_beans_index(request):
  coffee_beans = CoffeeBean.objects.all()
  coffee_bean_filter = CoffeeBeanFilter(request.GET, queryset=coffee_beans)
  coffee_beans = coffee_bean_filter.qs
  context = {
    'coffee_bean_filter': coffee_bean_filter,
    'coffee_beans': coffee_beans
  }
  return render(request, 'coffee_beans/index.html', context )
```

>I rendered the filter in DTL as a form, defining the method as get as was defined in my view.

```py
<div class="filter">
    <form method="get" action="">
        {{coffee_bean_filter.form.as_p}}
        <button class="btn" type="submit">Filter</button>
    </form>
</div>
```

### Review Functionality

>First I created a review ModelForm in forms.py, including three fields for the user to populate in the form. As datetime would be automatically created upon form submission, I did not need to include this.

```py
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_body', 'stars']
```

>As we wanted the user to select from a dropdown of stars rather than the integers that were held in the database, I previously created a STARS list which I then assigned to the choices parameter in the model field, with a default value set to 5 stars.

```py
class Review(models.Model):
    datetime = models.DateField(auto_now_add=True, null=True)
    stars = models.CharField(max_length=2, choices=STARS, default=STARS[0][0])
    review_title = models.CharField(max_length=250)
    review_body = models.CharField(max_length=1000)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
```

>In my view function, I assigned my ReviewForm to a form variable with POST as the request method, and again ensured that my form.save() method included the commit parameter with a value set to false and redirected the user back to the same detail page where their review would be displayed after the hard save.

```py
def add_review(request, cafe_id):    
    form = ReviewForm(request.POST)
   
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.cafe_id = cafe_id
        new_review.save()
    return redirect('detail', cafe_id = cafe_id)
```

>Once my review form and list of reviews was rendering in the html file for the detail page, I created a script which would initialise the stars select element to be displayed upon page load.

```py
<script>
  let starsEl = document.getElementById("id_stars");
  M.FormSelect.init(starsEl);
</script>
```

### CSS with Materialize

>Myself and Rob worked on the layout and look of the app towards the end of the project, using Materialize cards and grids. Upon completion, I was not happy with the layout, and decided to go back in and tidy things up. Example of the cafe detail page below:

<img src="main_app\static\uploads\kaffinepage.PNG"/>

### Search

>First I created my search function, using a conditional statement to check if a search has been made, define the query, and then retrieve the cafe data, where the cafe_name field includes the search term (case insensitive). I then passed the query and data as parameters in the render method which would display the cafes in a template separate from the cafe/index.html file which I then created.

```py
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        cafes = Cafe.objects.filter(cafe_name__icontains=searched)
        return render(request, 'cafes/search.html', {'searched': searched, 'cafes': cafes})
    else:
        return render(request, 'cafes/search.html')
```

I then included the search bar in the cafe/index.html file, which would trigger the search function upon post.

```py
<div class="search-div">
    <form method="POST" action="{% url 'search' %}" class="d-flex search">
        {% csrf_token %}
        <input type="search" placeholder="Search for a cafe" class=" text-field" aria-label="Search" name="searched">
        <button type="submit" class="btn">Search </button>
    </form>
</div>
```

### Sign-up & Sign-In

>Unfortunately, the team member who was working on sign-up and sign-in was not able to complete this functionality in the required timeframe, and so I decided to take this on and implement the user & cafe owner sign-up and sign-in using django-shapeshifter to handle three forms in a single view. I chose the MultiFormView class-based view as we had two different users, and if the individual was signing up as a cafe owner, the cafe table in the database needed to be populated with data as well as the django auth_user table. This also meant we could include the LoginRequiredMixin that we were using in our other CBVs. First, I defined my forms in forms.py, I created ModelForms for the IsCafeOwnerForm (populates the respective table in the database with a boolean value of true or false) and the CafeForm (populates the respective table in the database with the cafe information if the user is signing up as a cafe owner). I used the UserCreationForm from django.contrib.auth.forms to create a user with no special privileges from the username and password. I used the self.cleaned_data method to ensure a dictionary of validated form input field data was returned with their values, with conditional statements to ensure that: the username and email did not already exist, and that the passwords entered by the user were a match before creating an instance of the user.

```py
    username = forms.CharField(label='Choose a username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
   
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
class IsCafeOwnerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['is_cafe_owner']
 
class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['cafe_name', 'cafe_bio', 'date_founded', 'address_line_1', 'address_line_2', 'address_city', 'address_county', 'address_country', 'address_postcode', 'cafe_image', 'menu_image', 'cafe_website']
```

>Then in views.py, I imported my forms and MultiFormView from django-shapeshifter views. In my CBV for signup, I defined my form_classes, the name of the template to render and the success url. I then defined the form_valid method where I used conditional statements to check if the form submission is valid and then save that data in the database, and the super().forms_valid() method after login to insert the logged-in user id into the form fields.

```py
class SignUpFormsView(MultiFormView):
    form_classes = (UserRegisterForm, IsCafeOwnerForm, CafeForm)
    template_name = 'registration/signup.html'
    success_url = '/cafes/'
                   
    def forms_valid(self):
        forms = self.get_forms()
        print(forms)
        userRegisterForm = forms['userregisterform']
        isCafeOwnerForm = forms['iscafeownerform']
        cafeForm = forms['cafeform']
       
        if userRegisterForm.is_valid():
            user = userRegisterForm.save()
        if isCafeOwnerForm.is_valid():
            isCafeOwnerForm.save()  
        if cafeForm.is_valid():
            cafeForm.save()    
             
        login(self.request,user)    
        return super().forms_valid()
```

### User Profile

>Our app requires two types of user dashboard; the general user dashboard, and the cafe owner dashboard, as the latter is needed to provide the cafe owner with additional CRUD functionalities. In order to take a more streamlined approach, I decided to create just one url, view and template file which would be rendered dynamically depending on the type of user that is logged in. I defined the user from the request object, and the cafe record by filtering on the dataset where the user id was assigned to the cafe. As this just returns an empty array if no record was found, this would not return any error if the individual logged in was just a regular user.

```py
@login_required
def profile(request):
  user = request.user
  cafe = Cafe.objects.filter(user_id=user.id)[0]
  return render(request, 'users/profile/profile.html',{'user': user, 'cafe': cafe})
```

>The user dashboards were rendered dynamically by using simple conditional DTL statements:

```py
{% if cafe %}
```

>Example cafe owner dashboard below:

<img src="main_app\static\uploads\capture.PNG"/>

## Wins

### Troubleshooting & Bug fixing

>During this project I took the lead in supporting the team with technical issues which enhanced my troubleshooting skills and knowledge of git and django migrations. I was able to quickly disseminate a problem, and use my own knowledge and the help of google to find resolution to most issues without requiring the support of our instructor. Although this took up a significant amount of time, I am grateful for the opportunity it gave me to develop.

### Technical growth

>Aside from the technical skills I picked up from troubleshooting, this project was a steep learning curve in Python and Django, and by the end of the project I felt confident in using many of Python’s built in methods such as __str__(self) to convert the python objects from our models to strings and get_absolute_url()to generate unique URL patterns for each model record, as well as finding creative solutions to problems using Python libraries and applications.

## Challenges

### Leading the team

>I found being a team leader for this project challenging, particularly ensuring that deliverables were met in time for deployment. Going forward, I would ensure that I pushed to provide more hands-on support when I felt it was required, as although my approach was supportive, I left the responsibility for each team member to complete their deliverables in their hands.

### Migrations

>During the project we had several issues with database migrations. These issues arose from team members manually changing the tables in the database and rendering the html files with their updated field names, and deleting migration history in the project. Going forward, I would ensure to be clearer about the issues that making these changes would pose so we did not face the problems we did.

### Taking on additional work

>By the end of the project, I was not happy with the final product and felt that the time I spent providing technical support hindered my output. I spent an additional day completing the functionalities that were developed by the other team members such as: sign-up, sign-in, brewing method delete, and improving the layout and look of the site.

## Bugs

>The delete account functionality remains uncompleted.

## Future Enhancements

>- Favouriting: Going forward, I would like to provide the user with the option to favourite a cafe, and have this rendered in their user dashboard, where they then have the option to unfavourite it. I would also display a favourites count within the card of the cafe, on the cafe detail page, and in the cafe owner dashboard.
>- Cafe map: One of my stretch goals was to create a map of the Uk which displayed markers for each cafe which would link the user to the cafe detail page upon clicking. For this, I would use Mapbox or folium.
>- Search enhancement: The search functionality is currently basic, only allowing the user to search for cafes by cafe name. As a future enhancement, I would update my view function to search for every field in the cafe model from the search term, and also provide a search functionality for the coffee index page.

## Key Takeaways

>Team Leadership is not just about supporting, but ensuring the job gets done.
As mentioned, being a team leader was particularly challenging for me during this project, as I felt I lacked the confidence to be firm in regards to ensuring that functionalities were completed on time, and ensuring that my offer of support was taken when needed. Going forward, I would adapt my approach to ensure that I did not resort to taking on the work myself after the deadline had been completed.
