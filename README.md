Portfolio Project ALX Software Engineering 

Fertppm

APP link: https://fertppm.pythonanywhere.com/

Installation: pip install requirements.txt

License: GPL

![Alt text](image-2.png)

Research & project approval (Part 1-3)

Week 1: * Project proposal (staff review, approval required)
Week 2: * MVP (Minimum Viable Product) proposal (staff review, approval required)
Week 3: * Trello board (staff review, approval required)
Build Portfolio Project (Part 1-3)

Week 4: * Making Progress (status update, staff review)
Week 5: * MVP completed (staff review, approval required)
Week 6: * Landing page deployed * Final presentation preparation & delivery (staff review, approval required)

Week 7: * Blog post reflection (peer review) * github cleanup

End of Foundations Year

Authors:
<Benson Mwangi 
bensonmwangi101@gmail.com
bensonmwangi102@gmail.com
backend
>

<stephanie iman
Front end
>

<Benjamin Musyoki
benjaminmutunga40@gmail.com
Backend, Designer
>


echo "# Django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Benson480/Django.git
git push -u origin main


(env) PS C:\Django> git push -u origin main
Enumerating objects: 9315, done.
Counting objects: 100% (9315/9315), done.
Compressing objects: 100% (6011/6011), done.
Writing objects: 100% (9315/9315), 17.21 MiB | 622.00 KiB/s, done.
Total 9315 (delta 2232), reused 9315 (delta 2232), pack-reused 0
remote: Resolving deltas: 100% (2232/2232), done.
To https://github.com/Benson480/Fertigation_webapp.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(env) PS C:\Django> git push
Everything up-to-date



https://www.geeksforgeeks.org/how-to-deploy-django-project-on-pythonanywhere/

python3 -m venv env #create virtual environment
source env/bin/activate #activate virtual environment
cd deploy_on_pythonanywhere #navigate inside your project 
pip install -r requirements.txt #installing dependencies using requirements.txt


AI NAME
fertppm_ai_key 

AI KEY
<!-- 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 -->


git clone https://TOKEN@github.com/username/repository.git



Clear AXES Data: If you're testing and encountering these issues during development, you might want to clear the AXES data to reset the login attempts. Run the following command:

Copy code
python manage.py axes_reset



To freeze the currently installed Python packages into a requirements.txt file using pip, you can use the following command:

bash
Copy code
pip freeze > requirements.txt
This command will generate a requirements.txt file in the current directory containing a list of all the installed packages and their versions. Each line in the file will represent one package in the format package-name==version.

After running this command, you can use the requirements.txt file to recreate the same environment by installing the packages listed in it using pip. For example, to install the packages from requirements.txt into a virtual environment, you can use:

bash
Copy code
pip install -r requirements.txt
Make sure you run these commands in the appropriate directory or virtual environment where you want to create or update the requirements.txt file.