import valispace

deployment = input("Deployment Name:")
username = input("Username: ")
password = input("Password: ")

valispace = valispace.API(url="https://"+deployment+".valispace.com/", username=username, password=password)


# The ID of the Parent Component; If it is at the highest level, parent is null, but project need to be specified.
parent_component = 

# Object with the new Component Property
component = {
	"name": "NewCompentName",
	"parent": parent_component
}

# Function to get Vali by the fullname
componentPosted = valispace.post("components/", component)

