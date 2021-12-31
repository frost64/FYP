from textblob import TextBlob 

import listing
import update
import polarity


global pol
def reviews_list_polarity():
    for_reviews = []
    for_polarity = []
    super_list =listing.listing()
    updated_review_Dict = {}
    super_list_2 = []
#     print(super_list)
    for remove_none_type in super_list:
        if remove_none_type is not None:
            super_list_2.append(remove_none_type)
#             print(super_list_2)
    for select_list in super_list_2:
        for i in select_list:
            news =i.strip()
            new1=news.split(".")

            lst_list = []
            lst_list_2 = []


            for j in new1:
                j = update.updated_sentence(j)
                temp =j.replace("\r\n" ,"")
                # print(temp)
                pol = TextBlob(temp).sentiment.polarity
                pol=polarity.polarity_scaling(pol)
                tup = (temp ,pol)
                lst_list.append(tup)
            # print(lst[0])
                # lst_list[:-1]
            for remove_tuple in lst_list:
                if remove_tuple != ('',0):
                    lst_list_2.append(remove_tuple)
#             print(lst_list_2[0][0])
            if lst_list_2 != []:
                for_reviews.append(lst_list_2[0][0])
                for_polarity.append(lst_list_2[0][1])
            
            # individual_review.append(lst_list_2)
    updated_review_Dict["reviews"]=for_reviews
    updated_review_Dict["polarity"]=for_polarity
    
           
            # print(lst_list)
            # individual_review.append(lst_list)

    # return updated_review_Dict["reviews"],updated_review_Dict["polarity"]
    return updated_review_Dict
    # return individual_review
# reviews_list_polarity()
