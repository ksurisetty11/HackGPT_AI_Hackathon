def recommend_courses(user_skills, available_courses):
    reommendations = []
    for course in available_courses:
        overlap = set(user_skills).intersection(set(course['skills_required']))
        if overlap:
            recommendations.append({'course': course['name'], 'match_score': len(overlap)})
    return sorted(recommendations, key = lambda x: x['match_score'], reverse = True)
    