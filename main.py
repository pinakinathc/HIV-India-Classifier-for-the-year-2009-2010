import os
print "Execution started, Please wait..."
#os.system('python data_initializer.py')
#os.system('python semi_automated.py')

#The above 2 should be strictly commented to avoid losing manually labeled data
os.system('python data_generator.py')
# os.system('python data_corrector.py')
os.system('python main_classifier.py')
os.system('python plotting.py')
print "Execution over...Thank you for your time."