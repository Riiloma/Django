from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
    # return render(request,"about.html") 
    return HttpResponse("""
                        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid ">
            <a class="navbar-brand mx-4" href="#">VerdeVida</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse justify-content-end mx-4" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link " aria-current="page" href="#"><i class="fas fa-home"></i> Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="#"><i class="fas fa-scroll"></i> About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"> <i class="fas fa-inbox"></i> Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">
        <h1 class="text-start mt-4">About VerdeVida</h1>
        <div class="row mt-5">
            <h2>Proyects</h2>
            <div class="col-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>

            <div class="col-4 mt-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>

            <div class="col-4 mt-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>

            <div class="col-4 mt-4">
                <div class="card" style="width: 18rem;">
                    <img src="https://jardinessinfronteras.com/wp-content/uploads/2016/11/ecosistemas-acomo-cuidar-los-bosques.jpg?w=616&h=357" class="card-img-top" alt="paisaje verde">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                            the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12 mt-4">
                
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Error aut voluptatem rerum deleniti ad veritatis dicta et beatae nulla accusamus fugit saepe, quasi recusandae rem voluptates perspiciatis ipsam distinctio aliquam!</p>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <script src="https://kit.fontawesome.com/6a9d23ba8a.js" crossorigin="anonymous"></script>
</body>

</html>
                        """)