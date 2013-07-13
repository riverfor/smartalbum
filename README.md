Album Creator from Twitter

1 Introduction
    This is a django project, which can filter user's tweet by special words

    you can add the commond line into your crontab  "python manage.py getfromtwitter", but you need to run this commands manully first to generate the token twitter need

    
    This is only a draft version
        it contains the users=>albums data framework , you can add REST part if you want
        it contains the twitter filter part, which can save the url with the special tag into database.

        TODO: a) Analyze the photo number if meets the 100 / 200 / 300 /400 / 500
              b) Send a email with the special album link

2 Dependencies

    Python >= 2.6.8

    Django == 1.5.1
        pip install django == 1.5.1

    twitter == 1.0
        pip install twitter

    South
        pip install South



3 install
    edit albumcreator.sh, change to the right path
    add to your crontab
    */20 * * * * sh <youpath>/albumcreator.sh
