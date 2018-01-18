#!/usr/bin/python
import os
import commands

ROS2_GIT_PATH = "https://github.com/ros2/";
ROS2_REPO_FILE = "https://raw.githubusercontent.com/ros2/ros2/release-latest/ros2.repos";
ROS2_LOCAL_REPO_FILE = "ros2.repos"; 
OTC_CONTRIBUTORS = ["jwang11", "gaoethan"];
ROS2_LOCAL_PATH = "~/Working/ROS2";
TIME_DURATION = "--since=30.days.ago --until=now";
#dict_person = {"jwang11":0, "gaoethan":0};

if __name__=='__main__':
    os.chdir(r'/home/cathy/Working/ROS2/');
    cmd = r'%s %s' % ('rm',ROS2_LOCAL_REPO_FILE);
    os.system(cmd);
    cmd = r'%s %s' % ('wget', ROS2_REPO_FILE);
    os.system(cmd);

    fp = open(ROS2_LOCAL_REPO_FILE,'r');
    arr=[]
    dict_person = {};
    dict_project = {};
    for lines in fp.readlines():
        if "https://" in lines:
            git_url = lines.split(':',1)[1];
            
            git_name = os.path.split(git_url)[1];
            
            git_root = git_name.split('.')[0];
            print '%s %s' % ("git project:", git_root);
            print '%s %s' % ('OTC contribution during', TIME_DURATION);
            if (os.path.exists(git_root)):
                cmd = r'%s' % git_root;
                os.chdir(cmd);
                os.system('git pull');
            else: 
                cmd = r'%s %s' % ('git clone', git_url);
                os.system(cmd);
                cmd = r'%s' % git_root;
                os.chdir(cmd);

            
            for people in OTC_CONTRIBUTORS:
                cmd = r'%s %s %s %s' % ("git log", TIME_DURATION, "|grep -c", people);
                (status, output) = commands.getstatusoutput(cmd);
                print '%s %s %s %s' % (people, "contributed", output, "commits");

                if (int(output) and (git_root not in arr)):
                    arr.append(git_root);

                if int(output):
                    if (git_root not in dict_project):
                        dict_project[git_root] = int(output);
                    else:
                        dict_project[git_root] = dict_project[git_root] + int(output);
                    if (people not in dict_person):
                        dict_person[people] = int(output);
                    else:
                        dict_person[people] = dict_person[people] + int(output);

            print "============\n";


        os.chdir(r'/home/cathy/Working/ROS2/');

    print "Contributed to projects:",arr;
    print "Contributors:",dict_person;
    print "Project contribution:",dict_project;

    fp.close();


