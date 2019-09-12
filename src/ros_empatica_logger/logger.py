import rospy
from empatica_e4_msgs.msg import DataArrays
from datetime import datetime

file_list = ['accel_x', 'accel_y', 'accel_z', 'bvp', 'eda', 'ibi', 'skin_temp']

def init_log_files(datestring):
    for filename in file_list:
        with open(datestring + "_" + filename + ".csv", 'a+') as f:
            f.write('RosTime, PackageNr, EmpaticaTimestamp, ' + filename + '\n')

def callback(received_message):
    global datestring
    rostime = rospy.get_time()
    for key, data in zip(file_list,  [received_message.accel_x, received_message.accel_y,
                                      received_message.accel_z, received_message.bvp,
                                      received_message.eda, received_message.ibi,
                                      received_message.skin_temp]):
        if (data != []):
            with open(datestring + "_" + key + ".csv", 'a+') as f:
                for kk in range(len(data)):
                    f.write("%f, %d, %f, %f\n" % (rostime, received_message.count, received_message.timestamp, data[kk]))

def listener():
    global datestring
    datestring = datetime.now().isoformat()
    init_log_files(datestring)
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('physiology_data', DataArrays, callback)
    # keep this function/listener running the node is stopped by ROS master
    rospy.spin()
