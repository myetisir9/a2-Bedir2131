from bottle import request, route, run, debug, default_app

email = []
password = []
retpassword = []


def html(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                    <style style="text/css">

                   body, html {
                    height: 100%;
                    }

                   body {
                     background-image: url("https://bjk.com.tr/media/taraftar_media/taraftar-8959c92df2a0b89.jpg");
                     background-color: #cccccc;
                     background-repeat:no-repeat;
                      height: 100%;
                    background-size: cover;
                }

                  </style>
                  </head>

                  <body>
                      """
    page += content

    page += """
          </body>
          </html>"""

    return page


def index():
    welcome = "Welcome to my site!..."
    welcome += '''
        <form action="/Registration"  method="POST">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
    <hr>
    <p>By creating an account you agree to our <a href="/Contract">Terms & Privacy</a>.</p>

    <button type="submit" class="registerbtn">Register</button>
  </div>

  <div class="container signin">
    <p>Already have an account? <a href="/SignInForm">Sign in</a>.</p>
  </div>
</form>
    '''
    return html("Hello", welcome)


def Registration():
    email.append(request.forms.get('email'))
    password.append(request.forms.get('psw'))
    retpassword.append(request.forms.get('psw-repeat'))

    return index()


def SignInForm():
    signForm = '''

    <form action="/SignIn"  method="POST">
      <div>
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
      </div>
  </form>
  '''
    return signForm


def SignIn():
    tempemail = request.forms.get('username')
    temppassword = request.forms.get('password')

    for x in email:
        if x == tempemail:
            for y in password:
                if y == temppassword:
                    return web()
                else:
                    return html("Website", "Not Login!!!")

        else:
            return html("Website", "Not Login!!!")


def web():
    contentweb = """
       <!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8"/>
		<meta name="description" content="Welcome Besiktas fans">
		<link rel="stylesheet" type="text/css"  href="main.css">
		<title>ITÜ ÇARŞI FAN</title>
		<link rel="Shortcut Icon"  href="ıtu.png"  type="image/x-icon">
	</head>
	
	
	
	
	
	<body>
	
	<header>
	<div class="container">
	     <div class="logoo"><a target="blank" href="index.html"><img src="ıtu.png" alt="icon resmi"/></a></div>
		 <div class="search">
		 <input class="isearch" placeholder="Search...">
		 </div>
		 
	</div>
	</header>
	<div class="ayir"></div>
	<div class="resim">
	 
			 </div>
	   
	<ul class="menu">
	<li><a href="index.html">Home</a></li>
	<li><a target ="blank" href="hakkımızda.html">About Us</a></li>
	<li><a target ="blank" href="tarihçe.html">History</a>
	   <ul>
	       
		   <li>
		       <a target="blank" href="taraftar.html">History of Supporters</a>
		   </li>
		   <li>
		       <a target="blank" href="sampiyon.html">Championships</a>
		   </li>
		   </li> 
		</ul>   
	<li><a target="blank" href="video.html">Videos</a>
	   <ul>
	       <li>
		      <a href="mac-video.html">Game Videos</a>
		   </li>
		   <li>
		      <a target="blank" href="taraftar-video.html">Fan Videos</a>
		   </li>
	  
	   </ul>
	</li>
	    
	<li><a href="iletisim.html">Contact Us</a></li>
	</ul>
	
	<div class="container">
	<div class="left">
	    <div class="leftp" >
		<a target="blank" href="http://bjk.com.tr/tr"><img src="bjk1.jpg" alt="besiktas" width=100% height=710px; ></a>
	

		</div>
		</div>
		
		<div class="rigth">
	    <div class="rightp">
		<p><b><center><font size = "4" color= "brown" ><br></br> THE CLUB </font></center></b></p>
		
<p><Club Name	:	Beşiktaş Jimnastik Kulübü</p><br></br>
<p>Date of Foundation	:	1903</p><br></br>
<p>Colors  :	Black – White</p><br></br>
<p>Foundation Tittle	    :	Beşiktaş Bereket Jimnastik Kulübü</p><br></br>
<p>First President	    :	Mehmet Şamil Bey</p><br></br>
<P>First Championship :		Gymnastics 1911</p><br></br>
<p>Foundation Date of Football Branch	:	August 1911</p><br></br>
<p>First Football Championship Title	:	1919 Türk İdman Birliği League</p><br></br>
<p>Participation in Turkish League	:	1919</p>
		</div>
		</div>
		
	</div>
	<div class="clear"></div>
	
    <footer>
	<div class = "footer1">
		<ul>
		<li><a href="index.html">Home</a></li>
		<li><a href="hakkımızda.html">About Us</a></li>
		<li><a href="tarihçe.html">History</a></li>
		<li><a href="video.html">Videos</a></li>
		<li><a href="iletisim.html">Contact Us</a></li>
	</ul>
	
	
	<div class = "socialIcons">
		<a target="blank" href="https://www.facebook.com/groups/itulukartallar1903/"><img class="" alt="" src="facebook.png" width = "75" height = "75" align="center"/></a>
		<a target="blank" href="https://www.instagram.com/itulukartallar/?hl=tr	"><img class="" alt="" src="insta.png" width = "75" height = "75" /></a>
	</div>
	</div>
</footer>

	
	
	
	
	
		
	</body>

</html>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8"/>
		<link rel="stylesheet" href="main1.css">
		<meta name="description" content="Welcome Besiktas fans">
		<link rel="stylesheet" type="text/css"  href="main.css">
		<link rel="Shortcut Icon"  href="ıtu.png"  type="image/x-icon">
	</head>
	
	
	
	
	
	<body>
	
	<header>
	<div class="container">
	     <div class="logoo"><a target="blank" href="index.html"><img src="ıtu.png" alt="icon resmi"/></a></div>
		 <div class="search">
		 <input class="isearch" placeholder="Search...">
		 </div>
		 
	</div>
	</header>
	<div class="ayir"></div>
	<div class="resim">
	 
			 </div>
	   
	<ul class="menu">
	<li><a href="index.html">Home</a></li>
	<li><a target ="blank" href="hakkımızda.html">About Us</a></li>
	<li><a target ="blank" href="tarihçe.html">History</a>
	   <ul>
	       
		   <li>
		       <a target="blank" href="taraftar.html">History of Supporters</a>
		   </li>
		   <li>
		       <a target="blank" href="sampiyon.html">Championships</a>
		   </li>
		   </li> 
		</ul>   
	<li><a target="blank" href="video.html">Videos</a>
	   <ul>
	       <li>
		      <a href="mac-video.html">Game Videos</a>
		   </li>
		   <li>
		      <a target="blank" href="taraftar-video.html">Fan Videos</a>
		   </li>
	  
	   </ul>
	</li>
	    
	<li><a href="iletisim.html">Contact Us</a></li>
	</ul>
	
	
	<div class="container">
	<div class="left">
	    <div class="leftp" >
		<img src="taraftar2.jpg" alt="besiktas" width=100% height=600px;>
	

		</div>
		</div>
		
		<div class="rigth">
	    <div class="rightp">
		
		</div>
		</div>
<td style="width:50%; text-align:left; vertical-align:top;">
<ul><li><b><a title="Süper Lig">Turkish National Division</a>: 15</b> <br></li></ul>
<a>1957</a>,<a>1958</a>,1960</a>,1966</a>, 1967</a>, 1982</a>, 1986</a>, 1990</a>,<a>1991</a>,<a>1992</a>,<a>1995</a>,<a>2003</a>,<a>2009</a>,<a>2016</a>,<a>2017</a>

<ul><li><b><a title="Cumhurbaşkanlığı Kupası / Süper Kupa">Turkish Super Cup</a>: 8</b> <br></li></ul>
<a>1967,1974,1986,1989,1992,1994,1998,2006</a>

<ul><li><b><a title="Türkiye Futbol Şampiyonası">Turkish Football Championship</a>: 2</b> <br></li></ul>
<a>1934, 1951</a>

<ul><li><b><a title="Federasyon Kupası">Prime Minister's Cup</a>: 2</b> <br></li></ul>
<a>1957,1958</a>

<ul><li><b><a title="İstanbul Ligi">Istanbul Football League</a>: 11</b> <br></li></ul>
<a>1923-24,1933-34,1938-39,1939-40,1940-41,1941-42,1942-43,1944-45,1945-46,1949-50,1950-51</a>

<ul><li><b><a title="Pazar Ligi">Istanbul Shield</a>: 1</b> <br></li></ul>
<a>1921-22</a>

<ul><li><b><a title="Türkiye Futbol Şampiyonası">Istanbul Football Cup</a>: 2</b> <br></li></ul>
<a>1985,1988</a>

<ul><li><b><a title="Atatürk Kupası">Atatürk Cup</a>: 1</b> <br></li></ul>

<a>2000</a>
<p class="mw-empty-elt"></p>
</td>
	</div>
	<br></br><br></br>
	<img src="sampiyon.gif" alt"sampiyon" width="100%"; height="400px";>
	<div class="clear"></div>
	
    <footer>
	<div class = "footer1">
		<ul>
		<li><a href="index.html">Home</a></li>
		<li><a href="hakkımızda.html">About Us</a></li>
		<li><a href="tarihçe.html">History</a></li>
		<li><a href="video.html">Videos</a></li>
		<li><a href="iletisim.html">Contact Us</a></li>
	</ul>
	
	
	<div class = "socialIcons">
		<a target="blank" href="https://www.facebook.com/groups/itulukartallar1903/"><img class="" alt="" src="facebook.png" width = "75" height = "75" align="center"/></a>
		<a target="blank" href="https://www.instagram.com/itulukartallar/?hl=tr	"><img class="" alt="" src="insta.png" width = "75" height = "75" align="center"/></a>
	</div>
	</div>
</footer>

	
	
	
	
	
		
	</body>

</html>

        """
    return contentweb


route('/', 'GET', index)
route('/SignInForm', 'GET', SignInForm)
route('/SignIn', 'POST', SignIn)
route('/Registration', 'POST', Registration)

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
bapplication = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()