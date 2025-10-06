# Using .format(**dict) (clean way)

template="User {id} has {points} points and {role} role"
data={"id":403, "points":1245, "role":"admin"}

print(template.format(**data))

# Using f-strings with dict

msg=f'User {data["id"]} has {data["points"]} points and {data["role"]} role' 
print(msg)
