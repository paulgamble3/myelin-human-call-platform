import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./firebase/iso-eval-firebase-adminsdk-zs022-968af88ead.json")

if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL':"https://iso-eval-default-rtdb.firebaseio.com/"
        })

def write_task_item(item, task_name):
    ref = db.reference(task_name)
    ref.push(item)

def delete_item_by_ref(item_id, db_ref):
    ref = db.reference(db_ref)
    # Read the data at the posts reference (this is a blocking operation)
    result_ids = ref.get()
    z = db.reference(db_ref + '/' + item_id)
    result = z.delete()

def retrieve_data(db_ref, max_retrieve=False):

    # need some kind of caching here
    # but wait, is ref.get ordered by added
    #cached_data_path = './data/cached_results/' + db_ref + '.json'
    results = []
    # if os.path.exists(cached_data_path):
    #     with open(cached_data_path, 'r') as f:
    #         results = json.load(f)
    #         results = results['results']

    ref = db.reference(db_ref)
    # Read the data at the posts reference (this is a blocking operation)
    result_ids = ref.get()

    if result_ids is None:
        return []
    
    #print("result ids:", len(result_ids))
    for i, id in enumerate(result_ids):
        # if i < len(results):
        #     continue

        if i%100 == 0:
            print(i)
        z = db.reference(db_ref + '/' + id)
        result = z.get()

        #print(i, result['timestamp'])

        results.append({"id": id, "result": result})
        if max_retrieve and i > max_retrieve:
            break

    # with open(cached_data_path, 'w') as f:
    #     json.dump({'results': results}, f, indent=4)

    return results