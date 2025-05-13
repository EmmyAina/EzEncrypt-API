import subprocess

def encrypt_file(file_data, password, algo):

	# I cleaned the data to strip qouations and b string
	cleaned_data = file_data.strip().replace('"', '\\"')
	# used ~printf '%s'~ in prace of echo to avoid new line aes-256-cbc
	command = f"printf '%s' '{cleaned_data}' | openssl enc -aes-256-cbc -out helper/encoded.enc -pbkdf2 -pass pass:{password}"

	subprocess.run(command, shell=True)
def decrypt_file(file, password, algo):
	command = f"openssl enc -d -{algo} -in {file} -out mytext.txt -pbkdf2 -pass pass:{password} | perl -pe 'chomp if eof'"
	subprocess.run(command, shell=True)
