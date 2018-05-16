<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('pyrasample:static/pyramid-16x16.png')}">

    <title>A Sample application for the Pyramid Web Framework</title>

    <!-- Bootstrap core CSS -->
    <link href="${request.static_url('pyrasample:static/bootstrap.min.css')}?8" rel="stylesheet">
    <link href="${request.static_url('pyrasample:static/main.css')}?8" rel="stylesheet">

  </head>
  <body>
      <div class="container">
        <div class="row">
            ${ next.body() }
        </div>
      </div>
  </body>
</html>
