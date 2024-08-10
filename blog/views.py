from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
#from .models import Event

# Create your views here
# Generic Class example (PostList):
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

# Function-based view example (post_detail):
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()
    return render(request, "blog/post_detail.html",
                  {"post": post,
                   "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
    )

# class EventsList(generic.ListView):
#     model = Event
#     template_name = "index.html"
#     paginate_by = 12


# def event_detail(request, event_id):


#     # Database request
#     queryset = Event.object.filter.all()
#     event = get_object_or_404 (queryset, event_id = event_id)
#     # In this case, you could shorten the database request code by passing the model directly into the helper function.
#     # event = get_object_or_404(Event, event_id=event_id) // seria o mesmo pois o queryset faz o uso do all
#     return render(request, "events/event_detail.html." ,{"event":event})

