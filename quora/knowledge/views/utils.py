def vote(model_obj, req_post, user):
    if "upvote" in req_post:
        model_obj.upvotes += 1
        model_obj.upvote_users.add(user)
        model_obj.save()
    elif "downvote" in req_post:
        model_obj.downvotes += 1
        model_obj.downvote_users.add(user)
        model_obj.save()
    elif "remove_upvote" in req_post:
        model_obj.upvotes -= 1
        model_obj.upvote_users.remove(user)
        model_obj.save()
    elif "remove_downvote" in req_post:
        model_obj.downvotes -= 1
        model_obj.downvote_users.remove(user)
        model_obj.save()
