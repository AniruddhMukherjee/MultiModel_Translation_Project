# summerintership2024_21IT090

<h2>6th Sem Summer Internship</h2>
# 🌟 Machine Learning and Streamlit Internship 2024 - Project Showcase 🌟

Welcome to the UI Summer Internship 2024 GitHub repository! This project displays the work completed during the internship, together with useful knowledge and first-hand Streamlit experience.  

# Start of Internship

## 1️⃣ week 1
### *20th May 2024*
- *Orientation Meeting*: Introduction to Streamlit
- We discussed about the changes that i need to make in the UI of already built website to make it look better and more user friendly.

<img src="[https://media.licdn.com/dms/image/D5612AQEpoU1DdzX4yw/article-cover_image-shrink_600_2000/0/1654203654746?e=2147483647&v=beta&t=1WAkA9Pdvki3nSBEkXHCF7LkPrQvbmaeJu39czxaqpg](https://media.licdn.com/dms/image/D5612AQEpoU1DdzX4yw/article-cover_image-shrink_600_2000/0/1654203654746?e=2147483647&v=beta&t=1WAkA9Pdvki3nSBEkXHCF7LkPrQvbmaeJu39czxaqpg)" alt="Streamlit" width="300"/>


### *Here is the Outine of Week-1:*

1. Project Description
2. learning about the technologies being used
3. Learning the technologies
4. Making simple projects for project based learning
5. Learning new skills

## 📝 Day-by-Day Progress

### Day 1: Project Description 
- learned about the working of the website and the changes i am going to make in the website.
- started learning more about streamlit and how it is used in the industry.
- reading the streamlit documentation.

### Day 2: Self Learning
- Task of completely changing the UI using Figma was given to another intern and i was asked to wait till the design is made so that i can start working on that.
- During That time i started self learning process and learned about Deep Learning.
- Compeletd learning about Transformers.

### Day 3: Self Learning
- Another day of self learning and continued learning about transformer model for future use.

### Day 4: Self Learning

- Compeleted learning about Transformers and started learning about attention model.
- started basic practical learning about streamlit.
  
### Day 5: Stremlit Intro
- Started Learning about streamlit
- started finding good projects to make, to increase the knowledge of streamlit.
- continued learning about the attention model. 

- Here is the finalised link : http://52.63.0.141/personalpage.html


## 1️⃣ week 2
### *27th May 2024*
- *Orientation Meeting*: Introduction to AWS and overview of the internship tasks
- At the start of meeting I tackled questions regarding aws to know its base. Then the 1st week agenda regarding the tasks to be done was discussed. The tasks including from the start of creating an account to generating a portfolio hosted on a aws instance.

<img src="https://media.licdn.com/dms/image/D5612AQEpoU1DdzX4yw/article-cover_image-shrink_600_2000/0/1654203654746?e=2147483647&v=beta&t=1WAkA9Pdvki3nSBEkXHCF7LkPrQvbmaeJu39czxaqpg" alt="AWS Bootcamp" width="300"/>


### *Here is the Outine of Week-2:*

1. Create an AWS Free Tier account
2. Log on to the AWS Console
3. AWS Billing and Cost Management
4. Set up a zero-dollar limit budget
5. Launch an EC2 Instance
6. Connect to the EC2 Instance
7. Install Apache Web Server on the Linux Instance
8. Deploy a personal page.html on Apache
9. Open Security Group for Apache to accept connections on port 80
10. Access the page.html using the public IP address of the EC2 instance

## 📝 Day-by-Day Progress

### Day 1: Creating AWS Free Tier Account
- Created an AWS Free Tier account as part of Task 1.
- Logged on to the AWS Console (Task 2).
- Explored AWS Billing and Cost Management (Task 3).
- Set up a zero-dollar limit budget (Task 4).
- Launched an EC2 instance from the free tier options (Task 5).


### Day 2: creating instance with apache server to deploy web page
➠Connected to the EC2 Instance (Task 6):
- After launching the EC2 instance, I connected to it using SSH. This allowed me to access the virtual server, which is essentially a remote computer running on AWS infrastructure. The connection was established securely using the provided key pair, ensuring that my data remains protected.

➠ Commands : 
- shell- to write command in it
- pwd-current web directory
- whoami-this will which user is as logged in this account

➠ Installed an Apache Web Server on the Linux Instance (Task 7):
- Once connected, I installed Apache, a widely-used open-source web server software. Apache is crucial for serving web pages to users. The installation involved updating the package repositories and using package management commands to install Apache on the Linux-based EC2 instance.

➠ Commands : 
- sudo su-to elevate your credentials to root
- yum install -y httpd- to install apache web server(Linux server)
- cd /var/www/html- to create a HTML file into directory

➠Deployed a Personal page.html on Apache (Task 8):
- With Apache running, I deployed a simple HTML page (Personalpage.html). This involved placing the HTML file in Apache’s root directory and 
  configuring the server to serve this page. Deploying the HTML page allowed me to create a personal webpage accessible over the internet via 
  the EC2 instance's public IP address.

### Day 3: Building the Portfolio

➠ Setting Up the Project Structure:
- Created a project directory on the EC2 instance for the portfolio website. This included folders for HTML, CSS, JavaScript, and assets like images and fonts.
- Initialized the project with a basic index.html file to serve as the homepage.

➠ Creating the HTML Structure:
- Developed the initial structure of the portfolio using HTML5. This involved creating sections for the header, about me, projects, and contact information.
- Ensured the HTML code was semantic and well-organized to improve readability and SEO.

➠ Integrating Bootstrap:
- Incorporated Bootstrap, a popular CSS framework, to make the portfolio responsive and visually appealing.
Used Bootstrap components like navigation bars, cards, and buttons to enhance the design and functionality of the website.

### Day 4: Enhancing with JavaScript, SASS, and CSS

➠Adding Interactivity with JavaScript:
- Implemented JavaScript to add interactive features to the portfolio, such as form validation for the contact section and dynamic content loading for the projects section.
Utilized event listeners and DOM manipulation to create a more engaging user experience.

➠ Styling with SASS and CSS:
- Used SASS (Syntactically Awesome Style Sheets) to write more maintainable and modular CSS code. SASS variables, nesting, and mixins helped streamline the styling process.
- Compiled SASS files into CSS and applied custom styles to enhance the visual aesthetics of the portfolio. This included customizing Bootstrap themes and adding unique design elements.

➠ Finalizing the Deployment:
- Ensured all the files were correctly linked and the website was functioning as intended.
- Tested the portfolio on different browsers and devices to ensure compatibility and responsiveness.

➠Technologies Explored
- HTML5: Structured the content and elements of the portfolio.
- Bootstrap: Provided a responsive and modern design framework.
- JavaScript: Added interactivity and dynamic functionality to the website.
- SASS: Enhanced the CSS with advanced features for better maintainability and efficiency.
- CSS: Styled the website to improve visual appeal and user experience.

### Day 5: Configuration and final Touchup
- Configured the Security Group for the Apache server on the EC2 instance to accept incoming connections on port 80. This involved adding an inbound rule in the Security Group settings to allow HTTP traffic, ensuring that the web server is accessible from the internet.(Task 9)

- Verified the configuration by accessing the personal webpage hosted on the EC2 instance. Used the public IP address of the instance in a web browser to confirm that the Apache server is serving the webpage correctly. This demonstrated successful setup and configuration of the web server.(Task 10)

- Here is the finalised link : http://52.63.0.141/personalpage.html

## Notes:
➠We were given this repo which contains basic documentation of AWS services which can be helpful to everybody --
https://github.com/hamidgholami/accp-cheatsheet


## 1️⃣ week 3
### *03rd June 2024*
- *Orientation Meeting*: Introduction to AWS and overview of the internship tasks
- At the start of meeting I tackled questions regarding aws to know its base. Then the 3rd week agenda regarding the tasks to be done was discussed. The tasks including from the start of creating an account to generating a portfolio hosted on a aws instance.

<img src="https://media.licdn.com/dms/image/D5612AQEpoU1DdzX4yw/article-cover_image-shrink_600_2000/0/1654203654746?e=2147483647&v=beta&t=1WAkA9Pdvki3nSBEkXHCF7LkPrQvbmaeJu39czxaqpg" alt="AWS Bootcamp" width="300"/>


### *Here is the Outine of Week-3:*

1. Create an AWS Free Tier account
2. Log on to the AWS Console
3. AWS Billing and Cost Management
4. Set up a zero-dollar limit budget
5. Launch an EC2 Instance
6. Connect to the EC2 Instance
7. Install Apache Web Server on the Linux Instance
8. Deploy a personal page.html on Apache
9. Open Security Group for Apache to accept connections on port 80
10. Access the page.html using the public IP address of the EC2 instance

## 📝 Day-by-Day Progress

### Day 1: Creating AWS Free Tier Account
- Created an AWS Free Tier account as part of Task 1.
- Logged on to the AWS Console (Task 2).
- Explored AWS Billing and Cost Management (Task 3).
- Set up a zero-dollar limit budget (Task 4).
- Launched an EC2 instance from the free tier options (Task 5).


### Day 2: creating instance with apache server to deploy web page
➠Connected to the EC2 Instance (Task 6):
- After launching the EC2 instance, I connected to it using SSH. This allowed me to access the virtual server, which is essentially a remote computer running on AWS infrastructure. The connection was established securely using the provided key pair, ensuring that my data remains protected.

➠ Commands : 
- shell- to write command in it
- pwd-current web directory
- whoami-this will which user is as logged in this account

➠ Installed an Apache Web Server on the Linux Instance (Task 7):
- Once connected, I installed Apache, a widely-used open-source web server software. Apache is crucial for serving web pages to users. The installation involved updating the package repositories and using package management commands to install Apache on the Linux-based EC2 instance.

➠ Commands : 
- sudo su-to elevate your credentials to root
- yum install -y httpd- to install apache web server(Linux server)
- cd /var/www/html- to create a HTML file into directory

➠Deployed a Personal page.html on Apache (Task 8):
- With Apache running, I deployed a simple HTML page (Personalpage.html). This involved placing the HTML file in Apache’s root directory and 
  configuring the server to serve this page. Deploying the HTML page allowed me to create a personal webpage accessible over the internet via 
  the EC2 instance's public IP address.

### Day 3: Building the Portfolio

➠ Setting Up the Project Structure:
- Created a project directory on the EC2 instance for the portfolio website. This included folders for HTML, CSS, JavaScript, and assets like images and fonts.
- Initialized the project with a basic index.html file to serve as the homepage.

➠ Creating the HTML Structure:
- Developed the initial structure of the portfolio using HTML5. This involved creating sections for the header, about me, projects, and contact information.
- Ensured the HTML code was semantic and well-organized to improve readability and SEO.

➠ Integrating Bootstrap:
- Incorporated Bootstrap, a popular CSS framework, to make the portfolio responsive and visually appealing.
Used Bootstrap components like navigation bars, cards, and buttons to enhance the design and functionality of the website.

### Day 4: Enhancing with JavaScript, SASS, and CSS

➠Adding Interactivity with JavaScript:
- Implemented JavaScript to add interactive features to the portfolio, such as form validation for the contact section and dynamic content loading for the projects section.
Utilized event listeners and DOM manipulation to create a more engaging user experience.

➠ Styling with SASS and CSS:
- Used SASS (Syntactically Awesome Style Sheets) to write more maintainable and modular CSS code. SASS variables, nesting, and mixins helped streamline the styling process.
- Compiled SASS files into CSS and applied custom styles to enhance the visual aesthetics of the portfolio. This included customizing Bootstrap themes and adding unique design elements.

➠ Finalizing the Deployment:
- Ensured all the files were correctly linked and the website was functioning as intended.
- Tested the portfolio on different browsers and devices to ensure compatibility and responsiveness.

➠Technologies Explored
- HTML5: Structured the content and elements of the portfolio.
- Bootstrap: Provided a responsive and modern design framework.
- JavaScript: Added interactivity and dynamic functionality to the website.
- SASS: Enhanced the CSS with advanced features for better maintainability and efficiency.
- CSS: Styled the website to improve visual appeal and user experience.

### Day 5: Configuration and final Touchup
- Configured the Security Group for the Apache server on the EC2 instance to accept incoming connections on port 80. This involved adding an inbound rule in the Security Group settings to allow HTTP traffic, ensuring that the web server is accessible from the internet.(Task 9)

- Verified the configuration by accessing the personal webpage hosted on the EC2 instance. Used the public IP address of the instance in a web browser to confirm that the Apache server is serving the webpage correctly. This demonstrated successful setup and configuration of the web server.(Task 10)

- Here is the finalised link : http://52.63.0.141/personalpage.html

## Notes:
➠We were given this repo which contains basic documentation of AWS services which can be helpful to everybody --
https://github.com/hamidgholami/accp-cheatsheet


## 1️⃣ week 4
### *10th June 2024*
- *Orientation Meeting*: Introduction to AWS and overview of the internship tasks
- At the start of meeting I tackled questions regarding aws to know its base. Then the 4th week agenda regarding the tasks to be done was discussed. The tasks including from the start of creating an account to generating a portfolio hosted on a aws instance.

<img src="https://media.licdn.com/dms/image/D5612AQEpoU1DdzX4yw/article-cover_image-shrink_600_2000/0/1654203654746?e=2147483647&v=beta&t=1WAkA9Pdvki3nSBEkXHCF7LkPrQvbmaeJu39czxaqpg" alt="AWS Bootcamp" width="300"/>


### *Here is the Outine of Week-4:*

1. Create an AWS Free Tier account
2. Log on to the AWS Console
3. AWS Billing and Cost Management
4. Set up a zero-dollar limit budget
5. Launch an EC2 Instance
6. Connect to the EC2 Instance
7. Install Apache Web Server on the Linux Instance
8. Deploy a personal page.html on Apache
9. Open Security Group for Apache to accept connections on port 80
10. Access the page.html using the public IP address of the EC2 instance

## 📝 Day-by-Day Progress

### Day 1: Creating AWS Free Tier Account
- Created an AWS Free Tier account as part of Task 1.
- Logged on to the AWS Console (Task 2).
- Explored AWS Billing and Cost Management (Task 3).
- Set up a zero-dollar limit budget (Task 4).
- Launched an EC2 instance from the free tier options (Task 5).


### Day 2: creating instance with apache server to deploy web page
➠Connected to the EC2 Instance (Task 6):
- After launching the EC2 instance, I connected to it using SSH. This allowed me to access the virtual server, which is essentially a remote computer running on AWS infrastructure. The connection was established securely using the provided key pair, ensuring that my data remains protected.

➠ Commands : 
- shell- to write command in it
- pwd-current web directory
- whoami-this will which user is as logged in this account

➠ Installed an Apache Web Server on the Linux Instance (Task 7):
- Once connected, I installed Apache, a widely-used open-source web server software. Apache is crucial for serving web pages to users. The installation involved updating the package repositories and using package management commands to install Apache on the Linux-based EC2 instance.

➠ Commands : 
- sudo su-to elevate your credentials to root
- yum install -y httpd- to install apache web server(Linux server)
- cd /var/www/html- to create a HTML file into directory

➠Deployed a Personal page.html on Apache (Task 8):
- With Apache running, I deployed a simple HTML page (Personalpage.html). This involved placing the HTML file in Apache’s root directory and 
  configuring the server to serve this page. Deploying the HTML page allowed me to create a personal webpage accessible over the internet via 
  the EC2 instance's public IP address.

### Day 3: Building the Portfolio

➠ Setting Up the Project Structure:
- Created a project directory on the EC2 instance for the portfolio website. This included folders for HTML, CSS, JavaScript, and assets like images and fonts.
- Initialized the project with a basic index.html file to serve as the homepage.

➠ Creating the HTML Structure:
- Developed the initial structure of the portfolio using HTML5. This involved creating sections for the header, about me, projects, and contact information.
- Ensured the HTML code was semantic and well-organized to improve readability and SEO.

➠ Integrating Bootstrap:
- Incorporated Bootstrap, a popular CSS framework, to make the portfolio responsive and visually appealing.
Used Bootstrap components like navigation bars, cards, and buttons to enhance the design and functionality of the website.

### Day 4: Enhancing with JavaScript, SASS, and CSS

➠Adding Interactivity with JavaScript:
- Implemented JavaScript to add interactive features to the portfolio, such as form validation for the contact section and dynamic content loading for the projects section.
Utilized event listeners and DOM manipulation to create a more engaging user experience.

➠ Styling with SASS and CSS:
- Used SASS (Syntactically Awesome Style Sheets) to write more maintainable and modular CSS code. SASS variables, nesting, and mixins helped streamline the styling process.
- Compiled SASS files into CSS and applied custom styles to enhance the visual aesthetics of the portfolio. This included customizing Bootstrap themes and adding unique design elements.

➠ Finalizing the Deployment:
- Ensured all the files were correctly linked and the website was functioning as intended.
- Tested the portfolio on different browsers and devices to ensure compatibility and responsiveness.

➠Technologies Explored
- HTML5: Structured the content and elements of the portfolio.
- Bootstrap: Provided a responsive and modern design framework.
- JavaScript: Added interactivity and dynamic functionality to the website.
- SASS: Enhanced the CSS with advanced features for better maintainability and efficiency.
- CSS: Styled the website to improve visual appeal and user experience.

### Day 5: Configuration and final Touchup
- Configured the Security Group for the Apache server on the EC2 instance to accept incoming connections on port 80. This involved adding an inbound rule in the Security Group settings to allow HTTP traffic, ensuring that the web server is accessible from the internet.(Task 9)

- Verified the configuration by accessing the personal webpage hosted on the EC2 instance. Used the public IP address of the instance in a web browser to confirm that the Apache server is serving the webpage correctly. This demonstrated successful setup and configuration of the web server.(Task 10)

- Here is the finalised link : http://52.63.0.141/personalpage.html

## Notes:
➠We were given this repo which contains basic documentation of AWS services which can be helpful to everybody --
https://github.com/hamidgholami/accp-cheatsheet
