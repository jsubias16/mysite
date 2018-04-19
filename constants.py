import course

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='History',
                  teacher_name='Mr. Kileen',
                  resource_name='ArtHistory.net',
                  resource_url='http://www.arthistory.net/'),
    course.Course(period=3,
                  name='Algebra 2',
                  teacher_name='Mr. Shelton',
                  resource_name='Spark Notes',
                  resource_url='http://www.sparknotes.com/'),
    course.Course(period=4,
                  name='English',
                  teacher_name='Ms. Johnson',
                  resource_name='Interactive simulations',
                  resource_url='https://phet.colorado.edu/en/simulations/category/physics'),
    course.Course(period=5,
                  name='Biotech',
                  teacher_name='Mr. Ng',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/geometry'),
    course.Course(period=6,
                  name='AVID',
                  teacher_name='Ms. Johnson',
                  resource_name='Wikipedia',
                  resource_url='https://en.wikipedia.org/wiki/Biology'),
]