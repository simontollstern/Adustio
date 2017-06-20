// editpost.html
function insertExistingData(post) {
  //Inserts the current value of each field from the database and puts it into the input element of each field
  var title = document.getElementById('id_title')
  title.value = '{{ post.title }}'

  var text = document.getElementById('id_text')
  text.value = '{{ post.text }}'

  var youtube = document.getElementById('id_youtube')
  youtube.value = '{{ post.youtube }}'

  var soundcloud = document.getElementById('id_soundcloud')
  soundcloud.value = '{{ post.soundcloud }}'

  var pinned = document.getElementById('id_pinned')
  pinned.checked = False
}
