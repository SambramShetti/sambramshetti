# ----------------------------------------Upload files in AWS client Start--------------------------------------------------------------

# import boto3

# client = boto3.client('s3')

# # response = client.upload_file('E:\Resume\Jnr_software_resume.pdf', '2023-bucket.log', 'Jnr_software_resume.pdf')
# response = client.upload_file('E:\Resume\Jnr_software_resume.docx', '2023-bucket.log', 'Jnr_software_resume.docx')

# print(f"response: {response}")

# ----------------------------------------Upload files in AWS client End--------------------------------------------------------------



# ----------------------------------------Upload files in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

response = resource.Bucket("unique123-pythons").upload_file('E:\Resume\Appointment_Expirence_letter\TP_AppointmentLetter.pdf', 'TP_AppointmentLetter.pdf')

print(f"response: {response}")

# ----------------------------------------Upload files in AWS Resource End--------------------------------------------------------------
