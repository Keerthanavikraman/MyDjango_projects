from django.shortcuts import render

# Create your views here.

#8000/owner/books/add
def book_create(request):
    if request.method=="GET":
        return render(request,"book_add.html")
    elif request.method=="POST":
        #request.POST={"book_name":"randamoozham"}
        book_name=request.POST["book_name"]
        author_name=request.POST["author_name"]
        price = request.POST["price"]
        copies = request.POST["copies"]
        print(book_name,author_name,price,copies)
        return render(request,"book_add.html")



#8000/owner/books
def books_list(request):
    return render(request,"book_list.html")

#8000/owner/books/change/(id)
def book_update(request,id):
    return render(request,"book_edit.html")