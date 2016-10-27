'''
This module supports the logic to process a battery conversation
10/2016 Jerome Boyer - IBM
'''
from bmx_rs_client import RuleServiceClient


'''
   Main entry point to process the logic flow of the Battery Conversation
'''
def execute(assessment):
	# First assess what data to load
	rs=RuleServiceClient()
	a=rs.assessDataNeed(assessment)
	print(a)
	return a