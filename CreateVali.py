import valispace

deployment = input("Deployment Name:")
username = input("Username: ")
password = input("Password: ")

valispace = valispace.API(url="https://"+deployment+".valispace.com/", username=username, password=password)


# The ID of the Component where the Vali will be created
component_id = 

# Object with the new Vali Properties
vali = {
	"shortname": "Force",
	"formula": 10,
	"unit": "N",
	"parent": component_id
}

# Function to get Vali by the fullname
Vali = valispace.post("valis/", vali)

