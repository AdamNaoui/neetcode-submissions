class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_by_course={course:set() for course in range(numCourses) }
        dependents_by_prereqs={course:set() for course in range(numCourses) }

        for [course, prereq] in prerequisites:
            prereqs_by_course[course].add(prereq)
            dependents_by_prereqs[prereq].add(course)
        
        takeable_courses=[]
        taken_courses=set()

        for course,prereqs in prereqs_by_course.items():
            if len(prereqs)==0:
                takeable_courses.append(course)
        
        while takeable_courses:
            curr_course=takeable_courses.pop()
            if curr_course in taken_courses:
                continue
            
            taken_courses.add(curr_course)
            
            dependents=dependents_by_prereqs[curr_course]

            for dependent in dependents:
                prereqs_by_course[dependent].remove(curr_course)
                if len(prereqs_by_course[dependent])==0:
                    takeable_courses.append(dependent)

        return len(taken_courses)==numCourses

        