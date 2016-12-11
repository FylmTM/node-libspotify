{
  "targets": [
    {
      "target_name": "spotify",
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
            ]          }
        ],
        [
          'OS=="win"', {
            "libraries" : [
              '-lC:/build/libspotify/lib/libspotify.lib'
            ],
            "include_dirs": [
              'C:/build/libspotify/include'
            ]
          }
        ]
      ]
    },
    {
      'target_name': 'spotify-postbuild',
      'dependencies': ['spotify'],
      'conditions': [
        ['OS=="win"', {
          'copies': [{
            'destination': '<(PRODUCT_DIR)',
            'files': [
              'C:/build/libspotify/lib/libspotify.dll'
            ]
          }]
        }]
      ]
    }
  ]
}
