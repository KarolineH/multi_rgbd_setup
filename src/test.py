
#!/usr/bin/env python
import rospy

"""
Simply checks if both RGBD cameras are sreaming data
"""

cameras = ['/camera1','/camera2']

def check_stream():
    rospy.init_node('camera_stream_check', anonymous=True)
    for cam in cameras:
        camera_topics = rospy.get_published_topics(namespace=cam)
        if not camera_topics:
            print("%s is not publishing any data" %cam)
        else:
            print("%s is publishing %d topics" %(cam,len(camera_topics)))

if __name__ == "__main__":
    check_stream()
