{
  "targets": [
    {
      "target_name": "libspotify",
      "sources": [
        "src/album.cc",
        "src/artist.cc",
        "src/audio.cc",
        "src/binding.cc",
        "src/link.cc",
        "src/player.cc",
        "src/search.cc",
        "src/session.cc",
        "src/track.cc",
		"src/playlist.cc"
      ],
      "include_dirs" : [ 
        "<!(node -e \"require('nan')\")"
      ],
      "cflags": ["-Wall"],
      "conditions" : [
        [
          'OS!="win"', {
            "libraries" : [
              '<!@(pkg-config libspotify --libs)'
            ],
            "include_dirs": [
              '<!@(pkg-config libspotify --cflags | sed s/-I//g)'
            ]
          }
        ]
      ]
    }
  ]
}
