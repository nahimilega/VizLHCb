# VizLHCb


## Run the graph


## Decision 




# Question 1
The LHCb Online Tem to which you are currently applying has been designing for over 7 years a state-of-the art-cost-optimized data acquisition cluster. This system, when commissioned, will allegedly be the largest data acquisition machine in theWorld. The currently designed LHCb data acquisition must losslessly handle a constant flow of 32 Terabits of data and must perform a cluster-wide transposition in real-time.
This is because the data are scattered all over the LHCb detector and to analyze them, we must first assemble all the fragments from all the servers acquiring data."
Shortly describe in your own words (max 4 bullet points, each max 3 sentences) what in your opinion are the major NETWORK ENGINEERING challenges in this situation"
You may freely use any help on the web. I would suggest having a look at the project description first, including the PROVIDED LINKS


To evaluate the challenges, we would consider this problem with a spectrum of **Cost, Scalability, Reliability, Use case, Security and Maintenance.**

* Because data is received from event jets in real-time, protocol ensuring lossless transmission like **TCP cannot be used**. So the challenge is to ensure a lossless data transmission without packet drop. For that, we need to **identify bottlenecks and avoid network congestion** to avoid the queue being full at the node and eventually losing precious physics data. A topology with **even data flow distribution** is needed.

* Running the collider is an expensive task, and the data achieved is too precious. Therefore **backup networks are needed to avoid last-minute failure** leading to congestion at other parts of the network and increase reliability. 

* As the "interesting" events are singled out and stored, this adds on to the **datastream's busty nature**. Hence a **load balancing mechanism** would be needed to reduce sudden network congestion. Also, network topology should **not be too complex** and should maximise the use of **off the shelf components** to make the job of **maintenance easy**.
 
* The network **needs to be completely distributed** as the sheer amount of data rate is huge to communicate information back and forth central system. Also, the central model would be costly and limit the scalability in terms of the future expansion of data sensors. Similarly, keeping the the **disk buffer between L1 L2 and L3 triggers minimal** to reduce cost and make it scalable.

As it is a internal network security is not an issue here :)


## Ref
https://stackoverflow.com/questions/52615115/how-to-create-collapsible-box-in-pyqt
https://stackoverflow.com/questions/51154871/python-3-7-0-no-module-named-pyqt5-qtwebenginewidgets
https://www.tutorialspoint.com/