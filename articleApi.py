#####
##### API URL
##### https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
##### 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page=1'
#####

import requests
import json

def getUsernames(threshold):
        # set variables
        usernames = []
        page = 1
        totalPages = 1
        
        while page <= totalPages:
            # make request for each page
            pageRequest = requests.get('https:/jsonmock.hackerrank.com/api/article_users?page=' + str(page))
            articles = apiRequest.json()['data']

            # set totalPages value
            if page == 1:
                totalPages = apiRequest.json()['total_pages']

            # get data for each user
            for value in articles:
                submissionCount = value['submission_count']

                # check if submissionCount is greater than threshold
                # if it is, store in array of usernames
                if submissionCount > threshold:
                    usernames.append(value['username'])

            # go to next page
            page += 1
        
        return usernames


names = getUsernames(10)
print(names)
