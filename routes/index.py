# import pandas as pd
# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import requests
# from . import routes 
# from firebase_admin import auth, db
# import json

# # df = pd.read_csv("DataSet.csv",encoding='cp1252')
# df = [
#   {
#     "index": 0,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/specializations/deep-learning",
#     "keywords": "Tensorflow\nConvolutional Neural Network Artificial Neural Network\nDeep Learning\nBackpropagation\nPython Programming\nHyperparameter\nHyperparameter Optimization\nMachine Learning\nInductive Transfer Multi-Task Learning Facial Recognition System",
#     "language": "en",
#     "title": "Deep Learning Specialization",
#     "overview": "Deep Learning Specialization. Master Deep Learning, and Break into AI",
#     "instructor": "Andrew Ng"
#   },
#   {
#     "index": 1,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/python",
#     "keywords": "Json\nXml\nPython Programming\nDatabase (DBMS)\nPython Syntax And Semantics\nBasic Programming Language\nComputer Programming\nData Structure\nTuple Web Scraping Sqlite SQL",
#     "language": "en",
#     "title": "Python for Everybody Specialization",
#     "overview": "Learn to Program and Analyze Data with Python. Develop programs to gather, clean, analyze, and visualize data.",
#     "instructor": "Charles Russell Severance"
#   },
#   {
#     "index": 2,
#     "genres": "Information Technology",
#     "url": "https://www.coursera.org/professional-certificates/google-it-support",
#     "keywords": "Binary Code\nCustomer Support\nLinux\nTroubleshooting\nDomain Name System (DNS)\nIpv4\nNetwork Model\nPowershell\nLinux File Systems\nCommand-Line Interface\nDirectory Service\nLightweight Directory Access Protocol (LDAP)",
#     "language": "en",
#     "title": "Google IT Support Professional Certificate",
#     "overview": "The launchpad to a career in IT. This program is designed to take beginner learners to job readiness in about 3 to 6 months.",
#     "instructor": "Google"
#   },
#   {
#     "index": 3,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/specializations/applied-data-science",
#     "keywords": "Data Analysis\nPython Programming\nData Visualization (DataViz)\nMatplotlib\nData Science\nNumpy\nPandas\nPredictive Modelling\nModel Selection\nData Virtualization",
#     "language": "en",
#     "title": "Applied Data Science Specialization",
#     "overview": "Get hands-on skills for a Career in Data Science. Learn Python, analyze and visualize data. Apply your skills to data science and machine learning.",
#     "instructor": "IBM"
#   },
#   {
#     "index": 4,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/professional-certificates/applied-artifical-intelligence-ibm-watson-ai",
#     "keywords": "Data Science\nDeep Learning\nArtificial Intelligence (AI)\nMachine Learning\nWatson AI\nJobs\nApplication Programming Interfaces (API)\nwatson\nPython Programming\nNumpy\nPandas\nArtifical Intelligence",
#     "language": "en",
#     "title": "IBM Applied AI Professional Certificate",
#     "overview": "Kick-start Your Career with Artifical Intelligence",
#     "instructor": "IBM"
#   },
#   {
#     "index": 5,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/specializations/data-science-python",
#     "keywords": "Text Mining\nPython Programming\nPandas\nMatplotlib\nNumpy\nData Cleansing\nData Virtualization\nData Visualization (DataViz)\nMachine Learning (ML) Algorithms\nMachine Learning\nScikit-Learn\nNatural Language Toolkit (NLTK)",
#     "language": "en",
#     "title": "Applied Data Science with Python Specialization",
#     "overview": "Gain new insights into your data . Learn to apply data science methods and techniques, and acquire analysis skills.",
#     "instructor": "University of Michigan"
#   },
#   {
#     "index": 6,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/professional-certificates/ai-engineer",
#     "keywords": "Data Science\nDeep Learning\nArtificial Intelligence (AI)\nMachine Learning\nApache Spark\nBig Data\nSpark\nArtificial Neural Network\nkeras",
#     "language": "en",
#     "title": "IBM AI Engineering Professional Certificate",
#     "overview": "Launch Your Career in AI Engineering",
#     "instructor": "IBM"
#   },
#   {
#     "index": 7,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/java-programming",
#     "keywords": "Html\nJavaScript\nCascading Style Sheets (CCS)\nJava Programming\nHtml5\nAlgorithms\nProblem Solving\nString (Computer Science)\nData Structure\nCryptography\nHash Table\nProgramming Principles",
#     "language": "en",
#     "title": "Java Programming and Software Engineering Fundamentals Specialization",
#     "overview": "Explore a Career as a Software Engineer. Learn the basics of programming and software development",
#     "instructor": "Duke University"
#   },
#   {
#     "index": 8,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/full-stack-mobile-app-development",
#     "keywords": "Bootstrap (Front-End Framework)\nIonic (Mobile App Framework)\nNode.Js\nAngularjs\nJquery\nSASS (Stylesheet Language)\nReactive Programming\nTypescript\nApache Cordova\nMobile Application Development\nAuthentication\nMongodb",
#     "language": "en",
#     "title": "Full Stack Web and Multiplatform Mobile App Development Specialization",
#     "overview": "Build Complete Web and Hybrid Mobile Solutions. Master front-end web, hybrid mobile app and server-side development in five comprehensive courses.",
#     "instructor": "The Hong Kong University of Science and Technology"
#   },
#   {
#     "index": 9,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/full-stack-react",
#     "keywords": "Bootstrap (Front-End Framework)\nNode.Js\nReact (Javascript Library)\nRedux\nJquery\nSASS (Stylesheet Language)\nAuthentication\nMongodb\nExpress.Js",
#     "language": "en",
#     "title": "Full-Stack Web Development with React Specialization",
#     "overview": "Build Complete Web and Hybrid Mobile Solutions. Master front-end web, hybrid mobile app and server-side development in four comprehensive courses.",
#     "instructor": "The Hong Kong University of Science and Technology"
#   },
#   {
#     "index": 10,
#     "genres": "Game development",
#     "url": "https://www.coursera.org/specializations/game-development",
#     "keywords": "Video Game Development\nVideo Game Design\nUnity (User Interface)\nGame Design\nC Sharp (C#) (Programming Language)\nGame Design Document\nMarketing Communications\nProduct Development\nPlanning\nNew Product Development\nEntrepreneurship",
#     "language": "en",
#     "title": "Game Design and Development Specialization",
#     "overview": "Build a Game Using Unity 3D. Design and create your own game, and bring it to market, in five hands-on courses.",
#     "instructor": "Michigan State University"
#   },
#   {
#     "index": 11,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/web-applications",
#     "keywords": "Jquery\nweb application development\nHypertext Preprocessor (PHP)\nJavaScript\nMySQL\nHtml\nCascading Style Sheets (CCS)\nPhpmyadmin\nRelational Database\nSQL\nCreate, Read, Update And Delete",
#     "language": "en",
#     "title": "Web Applications for Everybody Specialization",
#     "overview": "Build dynamic database-backed web sites.. Use PHP, MySQL, jQuery, and Handlebars to build web and database applications.",
#     "instructor": "University of Michigan"
#   },
#   {
#     "index": 12,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/web-design",
#     "keywords": "Web Development\nCascading Style Sheets (CCS)\nHtml5\nJavaScript\nResponsive Web Design\nWeb Design\nWeb Accessibility\nHtml\nStyle Sheets\nDocument Object Model (DOM)\nBootstrap (Front-End Framework)",
#     "language": "en",
#     "title": "Web Design for Everybody: Basics of Web Development & Coding Specialization",
#     "overview": "Learn to Design and Create Websites. Build a responsive and accessible web portfolio using HTML5, CSS3, and JavaScript",
#     "instructor": "University of Michigan"
#   },
#   {
#     "index": 13,
#     "genres": "web development",
#     "url": "https://www.coursera.org/specializations/website-development",
#     "keywords": "HTML/CSS\nMongodb\nMeteor\nAPIs\nJavaScript\nJquery\nHtml\nCascading Style Sheets (CCS)\nResponsive Web Design\nRouting\nWeb Development",
#     "language": "en",
#     "title": "Responsive Website Development and Design Specialization",
#     "overview": "Create an interactive user experience.. Learn the fundamentals of full stack web development in five comprehensive courses.",
#     "instructor": "University of London"
#   },
#   {
#     "index": 14,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/specializations/app-development",
#     "keywords": "Persistence\niOS App Development\nXcode\nSwift (Programming Language)\nSyntax\nComputer Programming\nCore Data\nUser Interface",
#     "language": "en",
#     "title": "iOS App Development with Swift Specialization",
#     "overview": "Launch Your Career in iOS. Start building iOS apps in Swift in just four courses.",
#     "instructor": "University of Toronto"
#   },
#   {
#     "index": 15,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/specializations/android-app-development",
#     "keywords": "Software Testing\nAndroid Software Development\nJava Programming\nJunit\nLogic Programming\nAndroid Studio\nObject-Oriented Programming (OOP)\nComputer Programming\nConcurrent Computing\nUnit Testing",
#     "language": "en",
#     "title": "Android App Development Specialization",
#     "overview": "Launch Your Android App Development Career. Master the knowledge and skills necessary to develop maintainable mobile computing apps",
#     "instructor": "Vanderbilt University"
#   },
#   {
#     "index": 16,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/specializations/ios-development",
#     "keywords": "User Interface Design (UI Design)\nObjective-C\nSwift (Programming Language)\nUser Interface\niOS App Development\nComputer Programming\nXcode",
#     "language": "en",
#     "title": "iOS Development for Creative Entrepreneurs Specialization",
#     "overview": "Build a Foundation in iOS. Go from Objective-C novice to iOS app developer in just five courses.",
#     "instructor": "University of California, Irvine"
#   },
#   {
#     "index": 17,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
#     "keywords": "Html\nJavaScript\nCss Frameworks\nCascading Style Sheets (CCS)",
#     "language": "en",
#     "title": "HTML, CSS, and Javascript for Web Developers",
#     "overview": "we will learn the basic tools that every web page coder needs to know.",
#     "instructor": "Johns Hopkins University"
#   },
#   {
#     "index": 18,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/html",
#     "keywords": "Web Design\nWeb Accessibility\nHtml\nHtml5",
#     "language": "en",
#     "title": "Introduction to HTML5",
#     "overview": "This is the first course in the Web Design For Everybody specialization.",
#     "instructor": "University of Michigan"
#   },
#   {
#     "index": 19,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/learn/java-for-android",
#     "keywords": "Logic Programming\nAndroid Studio\nJava Programming\nObject-Oriented Programming (OOP)",
#     "language": "en",
#     "title": "Java for Android",
#     "overview": "Learners will work on several hands-on projects throughout the MOOC.",
#     "instructor": "Vanderbilt University"
#   },
#   {
#     "index": 20,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/learn/website-coding",
#     "keywords": "Jquery\nHtml\nJavaScript\nCascading Style Sheets (CCS)",
#     "language": "en",
#     "title": "Responsive Website Basics: Code with HTML, CSS, and JavaScript",
#     "overview": "In this course you will learn three key website programming and design languages.",
#     "instructor": "University of London"
#   },
#   {
#     "index": 21,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/bootstrap-4",
#     "keywords": "Bootstrap (Front-End Framework)\nNode.Js\nJquery\nSASS (Stylesheet Language)",
#     "language": "en",
#     "title": "Front-End Web UI Frameworks and Tools: Bootstrap 4",
#     "overview": "This course will give you an overview of client-side web UI frameworks.",
#     "instructor": "The Hong Kong University of Science and Technology"
#   },
#   {
#     "index": 22,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/become-a-js-pro-7-skills",
#     "keywords": "Web Development\nFront And Back Ends\nWeb\nMobile Development\nJavaScript",
#     "language": "en",
#     "title": "Become a JavaScript Pro with these 7 Skills",
#     "overview": "you will gain hands-on experience with 7 essential JavaScript topics.",
#     "instructor": "Harrison Kong"
#   },
#   {
#     "index": 23,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/python-dynamic-html-web-server",
#     "keywords": "Dynamic Web Application\nPython Programming\nServer Programming\nPython Web Application\nWeb Server",
#     "language": "en",
#     "title": "Python Dynamic HTML Web Server",
#     "overview": "you will create a Python application in which you will create a simple HTTP server.",
#     "instructor": "David Dalsveen"
#   },
#   {
#     "index": 24,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/javascript-animation",
#     "keywords": "front-end\nWeb Development\nVideo Game Development\nData Visualization (DataViz)\nJavaScript",
#     "language": "en",
#     "title": "Javascript animation for websites, storytelling, data visualization and games",
#     "overview": "You�ll build your own animations used in telling stories.",
#     "instructor": "Ravi Puralena"
#   },
#   {
#     "index": 25,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/build-a-google-firebase-webapp",
#     "keywords": "Web Development\nDatabase (DBMS)\nfirebase\nMobile Development\nJavaScript",
#     "language": "en",
#     "title": "Build a Google Firebase Web Application",
#     "overview": "you will understand the fundamental of Google Firebase.",
#     "instructor": "Harrison Kong"
#   },
#   {
#     "index": 26,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/tables-and-forms-in-html",
#     "keywords": "Web Development\nHtml\nHTML Tables\nForm (Html)\nNotepad++",
#     "language": "en",
#     "title": "Tables and Forms in HTML",
#     "overview": "you will write the HTML code to incorporate tables and forms into a web page.",
#     "instructor": "Judy Richardson"
#   },
#   {
#     "index": 27,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/build-first-react-website",
#     "keywords": "Web Development\nHtml\nWeb Application\nReact (Javascript Library)\nJavaScript",
#     "language": "en",
#     "title": "Build Your First React Website",
#     "overview": "You will understand the fundamental of React.",
#     "instructor": "Harrison Kong"
#   },
#   {
#     "index": 28,
#     "genres": "web development",
#     "url": "https://www.coursera.org/projects/images-and-links-in-html",
#     "keywords": "Html\nhtml links\nhtml images\nWeb Development",
#     "language": "en",
#     "title": "Images and Links in HTML",
#     "overview": "you will write the HTML code to incorporate images and links into a web page.",
#     "instructor": "Judy Richardson"
#   },
#   {
#     "index": 29,
#     "genres": "Game development",
#     "url": "https://www.coursera.org/projects/create-basic-behavior-csharp-unity",
#     "keywords": "Unity\nVideo Game Development\nC Sharp (C#) (Programming Language)\nApplication development",
#     "language": "en",
#     "title": "Create basic behavior with C# in Unity",
#     "overview": "you will create a simple game environment.",
#     "instructor": "Edward Falzon"
#   },
#   {
#     "index": 30,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/projects/customer-journey-prototyping-in-xd",
#     "keywords": "User Experience (UX)\nUI\nAdobe\nXD",
#     "language": "en",
#     "title": "Customer Journey Prototyping in XD",
#     "overview": "you will be able to prototype your user journeys in XD.",
#     "instructor": "Emma Moore"
#   },
#   {
#     "index": 31,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/introcss",
#     "keywords": "Web Design\nStyle Sheets\nCascading Style Sheets (CCS)\nWeb Development",
#     "language": "en",
#     "title": "Introduction to CSS3",
#     "overview": "This course will show you the basics of Cascading Style Sheets (CSS3).",
#     "instructor": "University of Michigan logo\nUniversity of Michigan"
#   },
#   {
#     "index": 32,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/javascript",
#     "keywords": "Document Object Model (DOM)\nJavaScript\nWeb Development",
#     "language": "en",
#     "title": "Interactivity with JavaScript",
#     "overview": "This course will introduce you to the basics of the JavaScript language.",
#     "instructor": "University of Michigan logo\nUniversity of Michigan"
#   },
#   {
#     "index": 33,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/web-applications-php",
#     "keywords": "Hypertext Preprocessor (PHP)\nHtml\nCascading Style Sheets (CCS)",
#     "language": "en",
#     "title": "Building Web Applications in PHP",
#     "overview": "In this course, you'll explore the basic structure of a web application.",
#     "instructor": "University of Michigan logo\nUniversity of Michigan"
#   },
#   {
#     "index": 34,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/single-page-web-apps-with-angularjs",
#     "keywords": "Unit Testing\nJavaScript\nAngularjs\nWeb Development",
#     "language": "en",
#     "title": "Single Page Web Applications with AngularJS",
#     "overview": "In this course, we will explore the core design of AngularJS.",
#     "instructor": "Johns Hopkins University logo\nJohns Hopkins University"
#   },
#   {
#     "index": 35,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/intro-sql",
#     "keywords": "Phpmyadmin\nMySQL\nRelational Database\nSQL",
#     "language": "en",
#     "title": "Introduction to Structured Query Language (SQL)",
#     "overview": "In this course, you'll walk through installation steps for installing a text editor.",
#     "instructor": "University of Michigan logo\nUniversity of Michigan"
#   },
#   {
#     "index": 36,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/uva-darden-continous-delivery-devops",
#     "keywords": "Devops\nContinuous Delivery\nUnit Testing\nInfrastructure As Code\nSystem Testing",
#     "language": "en",
#     "title": "Continuous Delivery & DevOps",
#     "overview": "provide you with the interdisciplinary skill set to cultivate a continuous deployment capability in your organization.",
#     "instructor": "University of Virginia logo\nUniversity of Virginia"
#   },
#   {
#     "index": 37,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/rails-with-active-record",
#     "keywords": "Authentication\nActive Record Pattern\nRuby On Rails",
#     "language": "en",
#     "title": "Rails with Active Record and Action Pack",
#     "overview": "we will explore how to interact with relational databases by using Active Record.",
#     "instructor": "Johns Hopkins University logo\nJohns Hopkins University"
#   },
#   {
#     "index": 38,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/server-side-nodejs",
#     "keywords": "Authentication\nNode.Js\nMongodb\nExpress.Js",
#     "language": "en",
#     "title": "Server-side Development with NodeJS, Express and MongoDB",
#     "overview": "This course deals with all things server-side.",
#     "instructor": "The Hong Kong University of Science and Technology logo\nThe Hong Kong University of Science and Technology"
#   },
#   {
#     "index": 39,
#     "genres": "web development",
#     "url": "https://www.coursera.org/learn/ruby-on-rails-intro",
#     "keywords": "Ruby (Programming Language)\nRuby On Rails\nHeroku",
#     "language": "en",
#     "title": "Ruby on Rails: An Introduction",
#     "overview": "In this course, we will explore how to build web applications with the Ruby on Rails.",
#     "instructor": "Johns Hopkins University logo\nJohns Hopkins University"
#   },
#   {
#     "index": 40,
#     "genres": "Mobile Development",
#     "url": "https://www.coursera.org/learn/objective-c",
#     "keywords": "iOS App Development\nComputer Programming\nXcode\nObjective-C",
#     "language": "en",
#     "title": "Foundations of Objective-C App Development",
#     "overview": "An introduction to the Objective-C programming language.",
#     "instructor": "University of California, Irvine logo\nUniversity of California, Irvine"
#   },
#   {
#     "index": 41,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/specializations/ui-ux-design",
#     "keywords": "Website Wireframe\nstrategy\nUser Interface Design (UI Design)\nUser Experience (UX)\nUser Research\nGraphic Design\nAdobe XD\nAdobe Illustrator\nInVision\nMarvel\nAdobe Indesign\nTreejack",
#     "language": "en",
#     "title": "UI / UX Design Specialization",
#     "overview": "Design High-Impact User Experiences. Research, design, and prototype effective, visually-driven websites and apps.",
#     "instructor": "California Institute of the Arts logo\nCalifornia Institute of the Arts"
#   },
#   {
#     "index": 42,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/specializations/michiganux",
#     "keywords": "User Research\nAffinity Diagram\nhuman computer interaction\nUser Experience (UX)\nUser Experience Design (UXD)\nAdobe Photoshop",
#     "language": "en",
#     "title": "User Experience Research and Design Specialization",
#     "overview": "Begin your journey in UX Research and Design . Gain a solid foundation in UX Research and Design to create great products and advance your career.",
#     "instructor": "University of Michigan"
#   },
#   {
#     "index": 43,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/specializations/interaction-design",
#     "keywords": "Storyboarding\nHeuristic Evaluation\nR Programming\nA/B Testing\nRapid Prototyping\nPaper Prototyping\nUser Experience (UX)\nUser Experience Design (UXD)\nUser Interface\nUser Research\nPersona (User Experience)\nHuman�Computer Interaction",
#     "language": "en",
#     "title": "Interaction Design Specialization",
#     "overview": "Learn how to design great user experiences. Design that delights users",
#     "instructor": "University of California San Diego"
#   },
#   {
#     "index": 44,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/learn/fundamentals-of-graphic-design",
#     "keywords": "Creativity\nGraphics\nDesign Theory\nColor Theory",
#     "language": "en",
#     "title": "Fundamentals of Graphic Design",
#     "overview": "you will have learned how to explore and investigate visual representation",
#     "instructor": "California Institute of the Arts"
#   },
#   {
#     "index": 45,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/specializations/game-design",
#     "keywords": "Interactive Storytelling\nGame Design Document\nVideo Game Design\nGame Design\nVideo Game Development\nGameplay\nLevel Design\nArt",
#     "language": "en",
#     "title": "Game Design: Art and Concepts Specialization",
#     "overview": "Create Imaginative Games. Design a video game for independent distribution in just four courses.",
#     "instructor": "California Institute of the Arts"
#   },
#   {
#     "index": 46,
#     "genres": "Data Administration",
#     "url": "https://www.coursera.org/specializations/excel-vba-creative-problem-solving",
#     "keywords": "Microsoft Excel Vba\nComputer Programming\nProblem Solving\nArrays\nDebugging",
#     "language": "en",
#     "title": "Excel/VBA for Creative Problem Solving Specialization",
#     "overview": "Optimize Your Excel Spreadsheets With VBA. Learn how to automate your Excel spreadsheets with Visual Basic for Applications",
#     "instructor": "University of Colorado Boulder"
#   },
#   {
#     "index": 47,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/learn/visual-elements-user-interface-design",
#     "keywords": "User Interface Design (UI Design)\nUser Experience (UX)\nGraphic Design",
#     "language": "en",
#     "title": "Visual Elements of User Interface Design",
#     "overview": "you will be able to describe the key formal elements of clear, consistent, and intuitive UI design.",
#     "instructor": "California Institute of the Arts logo\nCalifornia Institute of the Arts"
#   },
#   {
#     "index": 48,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/learn/user-experience-design",
#     "keywords": "Usability\nUser Experience (UX)\nUser Experience Design (UXD)\nUser Interface",
#     "language": "en",
#     "title": "Introduction to User Experience Design",
#     "overview": "The focus of this course is to introduce the learner to User Experience (UX) Design",
#     "instructor": "Georgia Institute of Technology logo\nGeorgia Institute of Technology"
#   },
#   {
#     "index": 49,
#     "genres": "Game development",
#     "url": "https://www.coursera.org/learn/game-design",
#     "keywords": "Video Game Development\nGameplay\nVideo Game Design\nGame Design",
#     "language": "en",
#     "title": "Introduction to Game Design",
#     "overview": "This course is an introduction to the primary concepts of gaming",
#     "instructor": "California Institute of the Arts logo\nCalifornia Institute of the Arts"
#   },
#   {
#     "index": 50,
#     "genres": "UI/UX",
#     "url": "https://www.coursera.org/learn/image-making",
#     "keywords": "Adobe Indesign\nArt\nCreativity\nGraphics",
#     "language": "en",
#     "title": "Introduction to Imagemaking",
#     "overview": "This course for serious makers, and for students new to imagemaking.",
#     "instructor": "California Institute of the Arts logo\nCalifornia Institute of the Arts"
#   },
#   {
#     "index": 51,
#     "genres": "Network Engineering",
#     "url": "https://www.udacity.com/course/cloud-dev-ops-nanodegree--nd9991",
#     "keywords": "AWS Configuration Management with Anisble Continuous Integration  Continuous Deployment Microservices with Kubernetes CloudFormation",
#     "language": "en",
#     "title": "Cloud Dev Ops Engineer",
#     "overview": "Learn to design and deploy infrastructure as code",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 52,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011",
#     "keywords": "JavaScript HTML CSS Webpack Flexbox Node Object-Oriented Programming",
#     "language": "en",
#     "title": "Front End Web Developer",
#     "overview": "Learn how to build high quality websites and dynamic applications to create stunning user experiences for the web.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 53,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044",
#     "keywords": "Python JavaScript PostgreSQL Flask Docker Kubernetes",
#     "language": "en",
#     "title": "Full Stack Web Developer",
#     "overview": "Learn to design and develop powerful modern web applications",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 54,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/java-developer-nanodegree--nd035",
#     "keywords": "Java Spring Boot Rest API MySQL MongoDB",
#     "language": "en",
#     "title": "Java Developer",
#     "overview": "Learn enterprise scale back-end development with Java",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 55,
#     "genres": "Network Engineering",
#     "url": "https://www.udacity.com/course/cloud-developer-nanodegree--nd9990",
#     "keywords": "AWS Microservices Serverless Architecture Kubernetes",
#     "language": "en",
#     "title": "Cloud Developer",
#     "overview": "Cloud development is the foundation for the new world of software development.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 56,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/c-plus-plus-nanodegree--nd213",
#     "keywords": "Data Structures & Algorithms Memory Management Concurrency Object Oriented Programming C++",
#     "language": "en",
#     "title": "C++",
#     "overview": "Learn C++, a high-performance programming language",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 57,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256",
#     "keywords": "Data Structures and Algorithms Problem Solving Interview Practice Problems Python",
#     "language": "en",
#     "title": "Data Structures and Algorithms",
#     "overview": "Get hands-on practice with over 100 data structures and algorithm exercises",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 58,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-engineer-nanodegree--nd027",
#     "keywords": "https://www.udacity.com/course/data-engineer-nanodegree--nd027",
#     "language": "en",
#     "title": "Data Engineer",
#     "overview": "Data Engineering is the foundation for the new world of Big Data.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 59,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/intro-to-programming-nanodegree--nd000",
#     "keywords": "Introduction to Programming HTML CSS Python",
#     "language": "en",
#     "title": "Introduction to Programming",
#     "overview": "Udacity's Intro to Programming is your first step towards careers",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 60,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/ios-developer-nanodegree--nd003",
#     "keywords": "Swift programming Core Data UIKit iOS networking app publishing User interfaces Local Persistence APIs",
#     "language": "en",
#     "title": "iOS Developer",
#     "overview": "Master the Swift programming language",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 61,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/react-nanodegree--nd019",
#     "keywords": "React Redux React Native",
#     "language": "en",
#     "title": "React",
#     "overview": "Master this powerful UI library from Facebook",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 62,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309",
#     "keywords": "Ethereum Blockchain Blockchain Architecture Data Auditing",
#     "language": "en",
#     "title": "Blockchain Developer",
#     "overview": "Demand for blockchain developers is skyrocketing.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 63,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/android-developer-nanodegree-by-google--nd801",
#     "keywords": "Android Development Databases Android Networking Libraries Crash Analysis Multilingual Support Android Libraries Gradle APIs",
#     "language": "en",
#     "title": "Android Developer",
#     "overview": "Start your career as an Android developer.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 64,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803",
#     "keywords": "Android Development Java programming Android Studio XML layouts Android Views",
#     "language": "en",
#     "title": "Android Basics",
#     "overview": "No programming experience? No Problem! Start developing Android apps today.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 65,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230",
#     "keywords": "Artificial Intelligence 2D Medical Imaging 3D Medical Imaging Electronic Health Record Data Deep Learning Wearable Device Data Supervised Learning",
#     "language": "en",
#     "title": "AI for Healthcare",
#     "overview": "Be at the forefront of the revolution of AI in Healthcare, and transform patient outcomes. Enable enhanced medical decision-making powered by machine learning to build the treatments of the future.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 66,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131",
#     "keywords": "Edge AI Computer Vision Deep Learning Edge Computing AI Modeling Deep Neural Networks (DNN) Convolutional Neural Networks (CNN) IoT Intel� Distribution of OpenVINO� Toolkit Intel� DevCloud for the Edge",
#     "language": "en",
#     "title": "Intel� Edge AI for IoT Developers",
#     "overview": "Lead the development of cutting-edge Edge AI applications for the future of the Internet of Things.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 67,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230",
#     "keywords": "TensorFlow Deep Learning scikit-learn Supervised Learning Unsupervised Learning",
#     "language": "en",
#     "title": "Intro to Machine Learning with TensorFlow",
#     "overview": "Learn foundational machine learning techniques - from data manipulation to unsupervised and supervised algorithms.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 68,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/ai-product-manager-nanodegree--nd088",
#     "keywords": "AI Products Training ML Models Annotating Datasets Prototyping a Product",
#     "language": "en",
#     "title": "AI Product Manager",
#     "overview": "Learn to develop AI products that deliver business value. Build skills that help you compete in the new AI-powered world.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 69,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/intro-to-machine-learning-nanodegree--nd229",
#     "keywords": "Introduction to Machine Learning Supervised Learning Deep Learning Unsupervised Learning",
#     "language": "en",
#     "title": "Intro to Machine Learning with PyTorch",
#     "overview": "Learn foundational machine learning techniques -- from data manipulation to unsupervised and supervised algorithms.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 70,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/ai-programming-python-nanodegree--nd089",
#     "keywords": "Python NumPy Pandas Matplotlib PyTorch",
#     "language": "en",
#     "title": "AI Programming with Python",
#     "overview": "Learn Python, NumPy, pandas, Matplotlib, PyTorch, Calculus, and Linear Algebra�the foundations for building your own neural network.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 71,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/ai-for-trading--nd880",
#     "keywords": "Momentum Trading Strategy Smart Beta Alpha Factors Natural Language Processing Deep Learning Neural Networks",
#     "language": "en",
#     "title": "Artificial Intelligence for Trading",
#     "overview": "Complete real-world projects designed by industry experts",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 72,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/computer-vision-nanodegree--nd891",
#     "keywords": "Convolutional Neural Networks (CNN) Recurrent Neural Networks (RNN) Simultaneous Localization and Mapping (SLAM) Object Tracking Image Classification Deep Learning",
#     "language": "en",
#     "title": "Computer Vision",
#     "overview": "Master the computer vision skills behind advances in robotics and automation.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 73,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/natural-language-processing-nanodegree--nd892",
#     "keywords": "Machine Learning Speech Recognition Sentiment Analysis Machine Translation Part of Speech Tagging",
#     "language": "en",
#     "title": "Natural Language Processing",
#     "overview": "Master the skills to get computers to understand, process, and manipulate human language.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 74,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893",
#     "keywords": "Reinforcement Learning Neural Networks PyTorch Deep Q-Networks (DQN) Deep Deterministic Policy Gradients (DDPG)",
#     "language": "en",
#     "title": "Deep Reinforcement Learning",
#     "overview": "Learn the deep reinforcement learning skills that are powering amazing advances in AI.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 75,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898",
#     "keywords": "AI Algorithms Search Algorithms Optimization Planning Pattern Recognition",
#     "language": "en",
#     "title": "Artificial Intelligence",
#     "overview": "Learn essential Artificial Intelligence concepts from AI experts",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 76,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t",
#     "keywords": "Machine Learning Supervised Learning Unsupervised Learning Deep Learning",
#     "language": "en",
#     "title": "Machine Learning Engineer",
#     "overview": "Learn advanced machine learning techniques and algorithms",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 77,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/deep-learning-nanodegree--nd101",
#     "keywords": "Deep Learning Neural Networks Jupyter Notebooks CNNs GANs",
#     "language": "en",
#     "title": "Deep Learning",
#     "overview": "Deep learning is driving advances in artificial intelligence that are changing our world.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 78,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/ai-for-business-leaders--nd054",
#     "keywords": "Artificial Intelligence Machine Learning Business Strategy Data Labeling Data Modeling",
#     "language": "en",
#     "title": "AI for Business Leaders",
#     "overview": "Master the foundations of artificial intelligence so you can strategically implement AI in your company.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 79,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/learn-sql--nd072",
#     "keywords": "SQL PostgreSQL JOINs Subqueries Window Functions Partitions Data Cleaning DDL DML Relational and Non-Relational Databases",
#     "language": "en",
#     "title": "SQL",
#     "overview": "Master SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 80,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-streaming-nanodegree--nd029",
#     "keywords": "Data Streaming Spark Kafka Kafka Streaming Spark Streaming",
#     "language": "en",
#     "title": "Data Streaming",
#     "overview": "Learn the skills to take you into the next era of data engineering.\nBuild real-time applications to process big data at scale.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 81,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/business-analytics-nanodegree--nd098",
#     "keywords": "Excel & Spreadsheets SQL Data Visualization Data Dashboards",
#     "language": "en",
#     "title": "Business Analytics",
#     "overview": "Gain foundational data skills applicable to any industry.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 82,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118",
#     "keywords": "R SQL Git",
#     "language": "en",
#     "title": "Programming for Data Science with R",
#     "overview": "Prepare for a data science career by learning the fundamental data programming tools: R, SQL, command line, and git.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 83,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-scientist-nanodegree--nd025",
#     "keywords": "Machine Learning Deep Learning Software Engineering",
#     "language": "en",
#     "title": "Data Scientist",
#     "overview": "Gain real-world data science experience with projects designed by industry experts. Build your portfolio and advance your data science career.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 84,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-visualization-nanodegree--nd197",
#     "keywords": "Data Visualization Tableau Dashboards Data Storytelling",
#     "language": "en",
#     "title": "Data Visualization",
#     "overview": "Combine data, visuals, and narrative to tell impactful stories and make data-driven decisions.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 85,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-analyst-nanodegree--nd002",
#     "keywords": "Data Wrangling Matplotlib Bootstrapping Pandas & NumPy Statistics",
#     "language": "en",
#     "title": "Data Analyst",
#     "overview": "Use Python, SQL, and statistics to uncover insights, communicate critical findings, and create data-driven solutions",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 86,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104",
#     "keywords": "Python Numpy & Pandas SQL Git & GitHub",
#     "language": "en",
#     "title": "Programming for Data Science with Python",
#     "overview": "Prepare for a data science career by learning the fundamental data programming tools: Python, SQL, command line, and git.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 87,
#     "genres": "Data Administration",
#     "url": "https://www.udacity.com/course/data-engineer-nanodegree--nd027",
#     "keywords": "Data Modeling Data Pipelines Data Lakes Spark Airflow",
#     "language": "en",
#     "title": "Data Engineer",
#     "overview": "Data Engineering is the foundation for the new world of Big Data.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 88,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/design-of-computer-programs--cs212",
#     "keywords": "Computer Program Design Python Design Process",
#     "language": "en",
#     "title": "Design Of Computer Programs",
#     "overview": "Programming Principles",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 89,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/intro-to-algorithms--cs215",
#     "keywords": "Algorithms Social Networks Graph Algorithms",
#     "language": "en",
#     "title": "Intro To Algorithms",
#     "overview": "This class will give you an introduction to the design and analysis of algorithms",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 90,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/software-testing--cs258",
#     "keywords": "Software Testing Debugging Code Coverage",
#     "language": "en",
#     "title": "Software Testing",
#     "overview": "How to Make Software Fail",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 91,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/software-debugging--cs259",
#     "keywords": "Debugging Python Automated Debugging",
#     "language": "en",
#     "title": "Software Debugging",
#     "overview": "Automating the Boring Tasks",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 92,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/intro-to-html-and-css--ud001",
#     "keywords": "HTML CSS CSS Syntax HTML Syntax Problem Set",
#     "language": "en",
#     "title": "Intro To HTML And CSS",
#     "overview": "you'll learn the fundamentals web development",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 93,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/full-stack-foundations--ud088",
#     "keywords": "Flask CRUD Model-View-Controller Python Object-relational Mapping",
#     "language": "en",
#     "title": "Full Stack Foundations",
#     "overview": "Build a data-driven web app with Python",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 94,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/objective-c-for-swift-developers--ud1009",
#     "keywords": "iOS Swift Objective-C Control Flow Syntax",
#     "language": "en",
#     "title": "Objective-C For Swift Developers",
#     "overview": "teach students how to understand and identify the differences between the Objective-C and Swift programming languages",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 95,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/swift-for-developers--ud1025",
#     "keywords": "Variables and Constants Strings Control Flow Functions",
#     "language": "en",
#     "title": "Swift For Developers",
#     "overview": "This course offers a quick practical introduction to Swift basics",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 96,
#     "genres": "UI/UX",
#     "url": "https://www.udacity.com/course/auto-layout--ud1026",
#     "keywords": "Design UI Stack Views Constraints",
#     "language": "en",
#     "title": "AutoLayout",
#     "overview": "Using Constraint-Based Design",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 97,
#     "genres": "Mobile Development",
#     "url": "https://www.udacity.com/course/server-side-swift--ud1031",
#     "keywords": "Swift Package Manager MySQL Docker Terraform Microservices",
#     "language": "en",
#     "title": "Server-Side Swift",
#     "overview": "Production-Ready Swift in the Cloud",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 98,
#     "genres": "web development",
#     "url": "https://www.udacity.com/course/asynchronous-javascript-requests--ud109",
#     "keywords": "Asynchronous Data Retrieval Ajax with XHR Ajax with jQuery Ajax",
#     "language": "en",
#     "title": "Asynchronous JavaScript Requests",
#     "overview": "Fetch Data Asynchronously",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 99,
#     "genres": "Network Engineering",
#     "url": "https://www.udacity.com/course/network-security--ud199",
#     "keywords": "Cryptography Systems Security Distributed Denial of Service",
#     "language": "en",
#     "title": "Network Security",
#     "overview": "This course provides an introduction to computer and network security.",
#     "instructor": "Udacity"
#   },
#   {
#     "index": 100,
#     "genres": "Network Engineering",
#     "url": "https://www.udacity.com/course/cyber-physical-systems-security--ud279",
#     "keywords": "Industrial Networks Industrial Control Systems Smart Grid",
#     "language": "en",
#     "title": "Cyber-Physical Systems Security",
#     "overview": "This course provides an introduction to security issues",
#     "instructor": "Udacity"
#   }
# ]
# features = ['keywords','genres', 'url', 'title', 'overview', 'instructor', 'language']

# @routes.route('/index/indexNewCourses', methods=['GET'])
# def indexNewCourses():
#     try:
#         for row in df:    
#             # for feature in features:
#             print('row', row)
#             userData = db.reference(path='courses/{0}'.format(row["index"])).set(row)
            
#             url = 'http://18.222.72.221:9200/courses/course/{0}'.format(row["index"])
#             obj = {
#                 "director": "director",
#                 "genres": row["genres"],
#                 "instructor": row["instructor"],
#                 "keywords": row["keywords"],
#                 "language": row["language"],
#                 "overview": row["overview"],
#                 "title": row["title"],
#                 "url": row["url"],
#                 "vote_average": "0",
#                 "vote_count": 0,
#                 "key": row["index"]
#             }

#             # print(obj)
#             # print(url)
#             headers = {"Content-Type": "application/json"}
#             x = requests.post(url, data=json.dumps(obj), headers=headers)
#             print(x.text)

#         # print('user',userData)
    
#         return {
#             "success": True,
#             "user": "asd"
#         }, 200
#     except Exception as e:
#         return {
#             "success": False,
#             "message": "{0}".format(e)
#         }, 400


# # def combine_features(row):
# #     return row['keywords']+" "+row['genres']

# # for feature in features:
# #     df[feature] = df[feature].fillna('') #filling all NaNs with blank string

# # df["combined_features"] = df.apply(combine_features,axis=1) 
# # df.iloc[0].combined_features
# # cv = CountVectorizer() #creating new CountVectorizer() object
# # count_matrix = cv.fit_transform(df["combined_features"])
# # cosine_sim = cosine_similarity(count_matrix)

# # def get_title_from_index(index):
# #     return df[df.index == index]["title"].values[0]

# # def get_index_from_title(title):
# #     return df[df.title == title]["index"].values[0]

# user_likes = ["Deep Learning Specialization","Python for Everybody Specialization"] # max 3 inputes 

# for course in user_likes:
#     course_index = get_index_from_title(course)
#     similar_courses = list(enumerate(cosine_sim[course_index]))
#     sorted_similar_courses = sorted(similar_courses,key=lambda x:x[1],reverse=True)[1:]
#     i=0
#     for element in sorted_similar_courses:
#         print(get_title_from_index(element[0]))
#         i=i+1
#         if i>2:
#             break