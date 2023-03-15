import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred= credentials.Certificate('iaad/fireSDK.json')
firebase_admin.initialize_app(cred,
 {
    'databaseURL': 'https://projetoiaad-default-rtdb.firebaseio.com/'
 }                       )

ref= db.reference('/')
ref.set({
    'employee':
    {
    'emp1': {
        'name':'Abino',
        'age': 22
    },
    'emp2': {
        'name': 'Joao',
        'age': 32
    }

    }
})

#atualização dos dados
ref= db.reference('employee')
emp_ref= ref.child('emp1')

emp_ref.update({
    'name': 'Abinoã'
})