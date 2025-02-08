syriac_letters = [
    # Format: (Syriac word, English meaning, audio file name, start time, end time)


    # Chapter 4, Pronouns
    # Page 21, Chaldean Grammar
    ("ܐܵܢܵܐ", "I", "audio_CG04.mp3", "1:24", "1:29"),
    ("ܐܵܝܸܬ", "You (m)", "audio_CG04.mp3", "1:30", "1:37"),
    ("ܐܵܝܲܬܝ", "You (f)", "audio_CG04.mp3", "1:38", "1:42"),
    ("ܐܵܗܘܼ", "He", "audio_CG04.mp3", "1:51", "1:55"), # problem none, i guess a taw + yoth = new symbol 
    ("ܐܵܗܝܼ", "She", "audio_CG04.mp3", "1:55", "1:58"),
    ("ܐܲܚܢܝܼܢ݇", "We", "audio_CG04.mp3", "2:00", "2:08"), # combined letters?
    ("ܐܲܟܼܬܘܼܢ", "You (pl.)", "audio_CG04.mp3", "2:08", "2:14"),
    ("ܐܲܗ݇ܢܝܼ", "They", "audio_CG04.mp3", "2:15", "2:20"),


    # Attached Possessive Pronouns  
    #ctrl+shift+p --> Insert Unicode: Insert --> 25CC for dotted cirlce 
    ("ܝܼ", "My", "audio_CG04.mp3", "5:48", "6:10"),
    ("‍ܘܼܟܼ", "Your (m)", "audio_CG04.mp3", "6:10", "6:23"),
    ("ܟܼܵ", "Your (f)", "audio_CG04.mp3", "6:23", "6:29"),
    ("ܗ◌ܹ", "His", "audio_CG04.mp3", "6:29", "6:36"), 
    ("ܗ̇◌ܵ", "Hers", "audio_CG04.mp3", "6:36", "6:42"),
    ("ܢ◌ܲ", "Our", "audio_CG04.mp3", "6:42", "6:46"),
    ("ܘܿܟܼܘܼܢ", "Your (pl)", "audio_CG04.mp3", "6:46", "6:52"),
    ("ܝܗܝ◌ܲ", "Their", "audio_CG04.mp3", "6:52", "6:58"),

    # Detached Possessive Pronouns   
    ("ܕܝܼܠܝܼ", "Of mine", "audio_CG04.mp3", "11:05", "11:11"),
    ("ܕܝܼܠܘܼܟܼ", "Of yours (m)", "audio_CG04.mp3", "11:11", "11:13"),
    ("ܕܝܼܠܲܟܼ", "Of yours (f)", "audio_CG04.mp3", "", ""),
    ("ܕܝܼܠܸܗ", "Of his", "audio_CG04.mp3", "11:13", "11:15"), 
    ("ܕܝܼܠܵܗ̇", "Of hers", "audio_CG04.mp3", "", "13:25"),
    ("ܕܝܼܠܲܢ", "Of ours", "audio_CG04.mp3", "11:15", "11:17"),
    ("ܕܝܼܠܘܿܟܼܘܼܢ", "Of yours (pl.)", "audio_CG04.mp3", "11:17", "11:19"),
    ("ܕܝܼܠܲܝܗܝ", "Of theirs", "audio_CG04.mp3", "11:19", "11:21"),

    # Demonstrative Pronouns 
    ("ܐܵܗ݇ܕ݂، ܐܵܗ݇ܕ݂ܝܼ", "This", "audio_CG04.mp3", "14:04", "14:23"),
    ("ܐܵܗܘܼ، ܐܵܗܘܵ", "That (m)", "audio_CG04.mp3", "15:01", "15:13"),
    ("ܐܵܗܝܼ، ܐܵܗܝܵ", "That (f)", "audio_CG04.mp3", "15:13", "15:17"),
    ("ܐܲܗ݇ܢ، ܐܲܗ݇ܢܝܼ", "These", "audio_CG04.mp3", "14:23", "14:38"), 
    ("ܐܵܗ݇ܢܲܝ", "Those", "audio_CG04.mp3", "15:37", "15:43"),

        
    # Interrogative Pronouns 
    ("ܡܲܢ، ܡܲܢܝܼ", "Who", "audio_CG04.mp3", "17:26", "17:34"),
    ("ܡܵܐ، ܡܲܗܵܐ", "What", "audio_CG04.mp3", "17:34", "17:37"),
    ("ܐܲܝܡܵܐ", "Which", "audio_CG04.mp3", "17:37", "17:44"),
    ("ܐܝܼܡܲܢ", "When", "audio_CG04.mp3", "17:44", "17:47"), 
    ("ܐܲܝܟܵܐ", "Where", "audio_CG04.mp3", "17:47", "17:53"),
    ("ܬܵܡܵܗܵܐ، ܩܲܝ", "Why", "audio_CG04.mp3", "17:53", "18:29"), 
    ("ܕܸܝܟܼ", "How", "audio_CG04.mp3", "18:29", "18:39"),

    # General Pronouns 
    ("ܚܲܕ݂݇", "One", "audio_CG04.mp3", "21:47", "21:57"),
    ("ܚܲܕ݂݇ ܐ݇ܢܵܫܵܐ", "Someone", "audio_CG04.mp3", "22:08", "22:19"),
    ("ܚܲܕ݂݇ܟܡܵܐ", "Some", "audio_CG04.mp3", "23:13", "23:23"),
    ("ܟܘܼܠ ܐܵܗ݇ܘܵ", "Each one", "audio_CG04.mp3", "22:53", "22:59"), 
    ("ܟܘܼܠ ܐ݇ܢܵܫܵܐ", "Everyone", "audio_CG04.mp3", "22:19", "22:31"),
    ("ܟܘܼܠ ܡܵܢܝܼ", "Everyone", "audio_CG04.mp3", "22:45", "22:53"), 
    ("ܟܘܼܠ ܡܸܢܕܝܼ", "Everything", "audio_CG04.mp3", "23:04", "23:09"),    
    ("ܟ̮ܘܼ ܐ݇ܢܵܫܵܐ", "No one", "audio_CG04.mp3", "22:31", "22:43"),
    ("ܟ̮ܘܼ ܡܸܢܕܝܼ", "Nothing", "audio_CG04.mp3", "23:09", "23:13"),
    ("ܠܵܐܚܲܕ݂݇", "No one", "audio_CG04.mp3", "21:57", "22:00"),
    ("ܡܸܢܕܝܼ", "Thing", "audio_CG04.mp3", "22:59", "23:04"), 
    ("ܦ̮ܠܵܢܵܝܵܐ", "So-and-so (m)", "audio_CG04.mp3", "21:18", "21:47"),
    ("ܦ̮ܠܵܢܵܝܬܼܵܐ", "So-and-so (f)", "audio_CG04.mp3", "21:18", "21:47"),
]
