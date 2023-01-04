import tensorflow as tf
tf.__version__

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))
device_name = tf.test.gpu_device_name()
print('Found GPU at: {}'.format(device_name))
