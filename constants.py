import course
import song

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

#Song class has title, artist_name, and youtube_url

TOP_TEN_SONGS = [
    song.Song(title="Psycho",
                artist_name="Post Malone",
                youtube_url="https://www.youtube.com/watch?v=au2n7VVGv_c"),
    song.Song(title="The Spotlight",
                artist_name="Logic",
                youtube_url="https://www.youtube.com/watch?v=fPEsDF5WL1w"),
    song.Song(title="Faint",
                artist_name="Linkin Park",
                youtube_url="https://www.youtube.com/watch?v=LYU-8IFcDPw"),
    song.Song(title="What I've Done",
                artist_name="Linkin Park",
                youtube_url="https://www.youtube.com/watch?v=8sgycukafqQ"),
    song.Song(title="Dead Memories",
                artist_name="Slipknot",
                youtube_url="https://www.youtube.com/watch?v=9gsAz6S_zSw"),
    song.Song(title="Remember The Name",
                artist_name="Fort Minor",
                youtube_url="https://www.youtube.com/watch?v=VDvr08sCPOc"),
    song.Song(title="Kenji",
                artist_name="Fort Minor",
                youtube_url="https://www.youtube.com/watch?v=pUBKcOZjX6g"),
    song.Song(title="Ride",
                artist_name="twenty one pilots",
                youtube_url="https://www.youtube.com/watch?v=Pw-0pbY9JeU"),
    song.Song(title="Before I forget",
                artist_name="Slipknot",
                youtube_url="https://www.youtube.com/watch?v=qw2LU1yS7aw"),
    song.Song(title="Sinner",
                artist_name="Veorra",
                youtube_url="https://www.youtube.com/watch?v=M99E8pgT3N4")
]
