# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:30:18 2020

@author: HARSHIT
"""
import os
import pafy
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def cliptube():
    
    if request.method=='POST':
        url=request.form.get('link')
        video = pafy.new(url)
        try:

            if request.form.get('video'):
                best=video.getbest()
                filename=best.download()
                links=best.url
                title=best.title
                extension=best.extension
                s=best.get_filesize()
                size=s//1000000
                return render_template('down.html',links=links,title=title,extension=extension,size=size)
                
            if request.form.get('audio'):    
                audio=video.getbestaudio()
                links=audio.url
                title=audio.title
                extension=audio.extension
                s=audio.get_filesize()
                size=s//1000000
                return render_template('down.html',links=links,title=title,extension=extension,size=size)
                #audio.download(filepath="C:\\Users\\HARSHIT\\youtube_downloader\\static")'''
        except ValueError:
            return "Incorrect URL"    
    return render_template('index.html')

@app.route('/down')
def down():
    return render_template('down.html')

if __name__=='__main__':
    app.run()
    # app.run(port=int(777),debug=True)


