from pyteamcity import TeamCity

tc = TeamCity("bekarazmadze", "Bequnio2001!", "http://localhost", 8111)

tc.get_project_by_project_id("AndroidToAndroid")