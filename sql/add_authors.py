from sql import db_session, User

authors = [
	{
		'first_name': 'Vasya',
		'last_name': 'Petrov',
		'email': 'Vasya@example.com',
	},
	{
		'first_name': 'Misha',
		'last_name': 'Ivanov',
		'email': 'Misha@example.com',
	},
	{
		'first_name': 'Anton',
		'last_name': 'Vasin',
		'email': 'Anton@example.com',
	}
]

for a in authors:
	author = User(a['first_name'], a['last_name'], a['email'],)
	db_session.add(author)

db_session.commit()