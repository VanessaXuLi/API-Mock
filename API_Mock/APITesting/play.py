Last login: Thu Feb 28 09:29:50 on ttys001
YingdeMacBook-Pro:~ yingxu$ cd Users/Shared/Jenkins/Home/secrets/initialAdminPassword
-bash: cd: Users/Shared/Jenkins/Home/secrets/initialAdminPassword: No such file or directory
YingdeMacBook-Pro:~ yingxu$ vim Users/Shared/Jenkins/Home/secrets/initialAdminPassword
YingdeMacBook-Pro:~ yingxu$ sudo cat /Users/Shared/Jenkins/Home/secrets/initialAdminPassword
Password:
cat: /Users/Shared/Jenkins/Home/secrets/initialAdminPassword: No such file or directory
YingdeMacBook-Pro:~ yingxu$ cd ..
YingdeMacBook-Pro:Users yingxu$ cd ..
YingdeMacBook-Pro:/ yingxu$ cd JENKINS_HOME/users/user.conf
-bash: cd: JENKINS_HOME/users/user.conf: No such file or directory
YingdeMacBook-Pro:/ yingxu$ cd Users/Shared/Jenkins/Home
YingdeMacBook-Pro:Home yingxu$ ls -l
total 160
-rw-r--r--    1 jenkins  jenkins   888  2 27 22:59 com.gitee.jenkins.connection.GiteeConnectionConfig.xml
-rw-r--r--    1 jenkins  jenkins   347  2 27 22:59 com.gitee.jenkins.trigger.GiteePushTrigger.xml
-rw-r--r--    1 jenkins  jenkins  1642  2 27 20:11 config.xml
-rw-r--r--    1 jenkins  jenkins  1379  2 27 20:01 credentials.xml
-rw-r--r--    1 jenkins  jenkins   156  2 27 20:11 hudson.model.UpdateCenter.xml
-rw-r--r--    1 jenkins  jenkins  1230  2 27 20:19 hudson.plugins.emailext.ExtendedEmailPublisher.xml
-rw-r--r--    1 jenkins  jenkins   370  2 27 17:05 hudson.plugins.git.GitTool.xml
-rw-------    1 jenkins  jenkins  1712  2 27 16:40 identity.key.enc
-rw-r--r--    1 jenkins  jenkins  1783  2 27 17:20 jenkins.install.InstallUtil.installingPlugins
-rw-r--r--    1 jenkins  jenkins     5  2 27 17:36 jenkins.install.InstallUtil.lastExecVersion
-rw-r--r--    1 jenkins  jenkins     5  2 27 17:36 jenkins.install.UpgradeWizard.state
-rw-r--r--    1 jenkins  jenkins   179  2 27 17:36 jenkins.model.JenkinsLocationConfiguration.xml
-rw-r--r--    1 jenkins  jenkins   171  2 27 16:40 jenkins.telemetry.Correlator.xml
drwxr-xr-x    4 jenkins  jenkins   128  2 27 20:00 jobs
drwxr-xr-x    4 jenkins  jenkins   128  2 27 20:41 logs
-rw-r--r--    1 jenkins  jenkins   907  2 27 20:11 nodeMonitors.xml
drwxr-xr-x    2 jenkins  jenkins    64  2 27 16:40 nodes
drwxr-xr-x  277 jenkins  jenkins  8864  2 28 01:59 plugins
-rw-r--r--@   1 root     jenkins  5554  2 27 19:41 postman_collection.json
-rw-r--r--@   1 root     jenkins   353  2 27 19:42 postman_globals.json
-rw-r--r--    1 jenkins  jenkins   130  2 28 09:35 queue.xml
-rw-r--r--    1 jenkins  jenkins   130  2 27 20:11 queue.xml.bak
-rw-r--r--    1 jenkins  jenkins    64  2 27 16:40 secret.key
-rw-r--r--    1 jenkins  jenkins     0  2 27 16:40 secret.key.not-so-secret
drwx------   13 jenkins  jenkins   416  2 28 09:56 secrets
drwxr-xr-x    7 jenkins  jenkins   224  2 27 20:08 updates
drwxr-xr-x    3 jenkins  jenkins    96  2 27 16:40 userContent
drwxr-xr-x    4 jenkins  jenkins   128  2 27 17:36 users
drwxr-xr-x   26 jenkins  jenkins   832  2 27 16:40 war
drwxr-xr-x    2 jenkins  jenkins    64  2 27 17:05 workflow-libs
drwxr-xr-x    4 jenkins  jenkins   128  2 27 20:18 workspace
YingdeMacBook-Pro:Home yingxu$ rm postman_collection.json
override rw-r--r--  root/jenkins for postman_collection.json? y
rm: postman_collection.json: Permission denied
YingdeMacBook-Pro:Home yingxu$ rm postman_globals.json
override rw-r--r--  root/jenkins for postman_globals.json? y
rm: postman_globals.json: Permission denied
YingdeMacBook-Pro:Home yingxu$ cd users
YingdeMacBook-Pro:users yingxu$ ls -l
total 8
drwx------  3 jenkins  jenkins   96  2 27 20:30 root_8749746190901527537
-rw-r--r--  1 jenkins  jenkins  298  2 27 17:36 users.xml
YingdeMacBook-Pro:users yingxu$ cd jenkins
-bash: cd: jenkins: No such file or directory
YingdeMacBook-Pro:users yingxu$ ls
root_8749746190901527537	users.xml
YingdeMacBook-Pro:users yingxu$ ls
root_8749746190901527537	users.xml
YingdeMacBook-Pro:users yingxu$ cd admin
-bash: cd: admin: No such file or directory
YingdeMacBook-Pro:users yingxu$ ls -l
total 8
drwx------  3 jenkins  jenkins   96  2 27 20:30 root_8749746190901527537
-rw-r--r--  1 jenkins  jenkins  298  2 27 17:36 users.xml
YingdeMacBook-Pro:users yingxu$ vim users.xml
YingdeMacBook-Pro:users yingxu$ cd ..
YingdeMacBook-Pro:Home yingxu$ cd ..
YingdeMacBook-Pro:Jenkins yingxu$ ls -l
total 0
drwxr-xr-x  39 jenkins  jenkins  1248  2 28 10:30 Home
drwxr-xr-x   8 jenkins  jenkins   256  2 28 10:29 tmp
YingdeMacBook-Pro:Jenkins yingxu$ cd ..
YingdeMacBook-Pro:Shared yingxu$ cd ..
YingdeMacBook-Pro:Users yingxu$ cd ..
YingdeMacBook-Pro:/ yingxu$ cd ....
-bash: cd: ....: No such file or directory
YingdeMacBook-Pro:/ yingxu$ cd ..
YingdeMacBook-Pro:/ yingxu$ cd ..
YingdeMacBook-Pro:/ yingxu$ ls -l
total 21
drwxrwxr-x+ 52 root  admin  1664  2 27 15:31 Applications
drwxr-xr-x+ 64 root  wheel  2048  2 27 15:45 Library
drwxr-xr-x   2 root  wheel    64 10  3  2017 Network
drwxr-xr-x@  4 root  wheel   128 10 26  2017 System
drwxr-xr-x   7 root  admin   224  2 25 15:11 Users
drwxr-xr-x+  3 root  wheel    96  2 27 18:46 Volumes
drwxr-xr-x@ 38 root  wheel  1216  2 25 14:59 bin
drwxrwxr-t   2 root  admin    64 10  3  2017 cores
dr-xr-xr-x   3 root  wheel  4508  2 27 16:25 dev
lrwxr-xr-x@  1 root  wheel    11 10 26  2017 etc -> private/etc
dr-xr-xr-x   2 root  wheel     1  2 28 10:07 home
-rw-r--r--   1 root  wheel   313  9  1  2017 installer.failurerequests
dr-xr-xr-x   2 root  wheel     1  2 28 10:07 net
drwxr-xr-x   6 root  wheel   192 10 26  2017 private
drwxr-xr-x@ 63 root  wheel  2016  2 25 14:59 sbin
lrwxr-xr-x@  1 root  wheel    11 10 26  2017 tmp -> private/tmp
drwxr-xr-x@ 10 root  wheel   320  2 27 15:45 usr
lrwxr-xr-x@  1 root  wheel    11 10 26  2017 var -> private/var
YingdeMacBook-Pro:/ yingxu$ cd users
YingdeMacBook-Pro:users yingxu$ ls -l
total 0
drwxr-xr-x+ 12 Guest   _guest  384  2 25 15:11 Guest
drwxrwxrwt   6 root    wheel   192  2 27 15:31 Shared
drwxr-xr-x+ 23 yingxu  staff   736  2 28 10:34 yingxu
drwxr-xr-x+ 12 yingyu  staff   384  2 22 18:42 yingyu
YingdeMacBook-Pro:users yingxu$ cd yingxu
YingdeMacBook-Pro:yingxu yingxu$ ls -l
total 0
drwx------@  4 yingxu  staff   128  2 25 14:02 Applications
drwx------+  8 yingxu  staff   256  2 25 16:36 Desktop
drwx------+  4 yingxu  staff   128  2 27 10:27 Documents
drwx------+ 21 yingxu  staff   672  2 27 16:39 Downloads
drwx------@ 61 yingxu  staff  1952  2 25 21:07 Library
drwx------+  3 yingxu  staff    96  2 22 19:36 Movies
drwx------+  3 yingxu  staff    96  2 22 19:36 Music
drwx------+  4 yingxu  staff   128  2 25 23:45 Pictures
drwxr-xr-x+  4 yingxu  staff   128  2 22 19:36 Public
drwxr-xr-x   6 yingxu  staff   192  2 26 14:39 PycharmProjects
YingdeMacBook-Pro:yingxu yingxu$ chmod 777 Downloads
YingdeMacBook-Pro:yingxu yingxu$ ls -l
total 0
drwx------@  4 yingxu  staff   128  2 25 14:02 Applications
drwx------+  8 yingxu  staff   256  2 25 16:36 Desktop
drwx------+  4 yingxu  staff   128  2 27 10:27 Documents
drwxrwxrwx+ 21 yingxu  staff   672  2 27 16:39 Downloads
drwx------@ 61 yingxu  staff  1952  2 25 21:07 Library
drwx------+  3 yingxu  staff    96  2 22 19:36 Movies
drwx------+  3 yingxu  staff    96  2 22 19:36 Music
drwx------+  4 yingxu  staff   128  2 25 23:45 Pictures
drwxr-xr-x+  4 yingxu  staff   128  2 22 19:36 Public
drwxr-xr-x   6 yingxu  staff   192  2 26 14:39 PycharmProjects
YingdeMacBook-Pro:yingxu yingxu$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
YingdeMacBook-Pro:yingxu yingxu$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
YingdeMacBook-Pro:yingxu yingxu$ cd downloads
YingdeMacBook-Pro:downloads yingxu$ ls
Chrome_353811052.apk			apache-jmeter-5.1			jdk-11.0.2_osx-x64_bin.dmg
MySales_TestCases1.xlsx			apache-jmeter-5.1.tgz			jdk-11.0.2_osx-x64_bin.tar.gz
MySales_TestCases_ver1.xlsx		apache-jmeter-5.1.zip			postmanAPI
Postman-osx-6.7.4.zip			cc-assistant-1.1.2.dmg			pycharm-professional-2018.3.4.dmg
Recents.app				googlechrome.dmg			shopee_kredit_testmodule.xlsx
Recents_latest.zip			jdk-11.0.2.jdk
YingdeMacBook-Pro:downloads yingxu$ cd postmanAPI/
YingdeMacBook-Pro:postmanAPI yingxu$ ls
newman			node_modules		package-lock.json	postman_collection.json	postman_globals.json
YingdeMacBook-Pro:postmanAPI yingxu$ pwd
/users/yingxu/downloads/postmanAPI
YingdeMacBook-Pro:postmanAPI yingxu$ sudo vim /usr/local/lib/node_modules/newman/node_modules/xmlbuilder/lib/XMLStringifier.js
Password:


    XMLStringifier.prototype.xmlStandalone = function(val) {
      if (this.options.noValidation) {
        return val;
      }
      if (val) {
        return "yes";
      } else {
        return "no";
      }
    };

    XMLStringifier.prototype.dtdPubID = function(val) {
      if (this.options.noValidation) {
        return val;
      }
      return this.assertLegalChar('' + val || '');
    };

    XMLStringifier.prototype.dtdSysID = function(val) {
      if (this.options.noValidation) {
        return val;
      }

