// Can you think of any potential errors on the client or server?
// Handle these on your own to improve user experience.

// UPDATE
// Challenge: Instead of using a new modal, try using the same modal for
// handling both POST and PUT requests.

// DELETE
// Instead of deleting on the button click, add a confirmation alert.
// Display a message saying, like "No books! Please add one.", when no books are present.

<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <alert :message='message' v-if='showMessage'></alert> <!-- alerts -->
                <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>
                  Add Book
                </button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Author</th>
                            <th scope="col">Read?</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(book, index) in books" :key="index">
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>
                                <span v-if="book.read">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <!-- <td>foo</td>
                            <td>bar</td>
                            <td>foobar</td> -->
                            <td>
                                <div class="btn-group" role="group">
                                    <!-- <button type="button" class="btn btn-warning btn-sm">
                                        Update
                                    </button> -->
                                    <button type="button" class="btn btn-warning btn-sm"
                                    v-b-modal.book-update-modal @click="editBook(book)">
                                      Update
                                    </button>
                                    <!-- <button type="button" class="btn btn-danger btn-sm">
                                        Delete
                                    </button> -->
                                    <button type="button" class="btn btn-danger btn-sm"
                                    @click="onDeleteBook(book)">
                                      Delete
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <b-modal ref="addBookModal"
                 id="book-modal"
                 title="Add a new book"
                 hide-footer>
          <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group"
                        label="Title:"
                        label-for="form-title-input">
            <b-form-input id="form-title-input"
                          type="text"
                          v-model="addBookForm.title"
                          required
                          placeholder="Enter title">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-author-group"
                        label="Author:"
                        label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
              <b-form-checkbox value="true">Read?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </b-modal>
        <b-modal ref="editBookModal"
                 id="book-update-modal"
                 title="Update"
                 hide-footer>
            <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
            <b-form-group id="form-title-edit-group"
                          label="Title: "
                          label-for="form-title-edit-input">
              <b-form-input id="form-title-edit-input"
                            type="text"
                            v-model="editForm.title"
                            required
                            placeholder="Enter title">
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-read-edit-group"
                          label="Author: "
                          label-for="form-author-edit-input">
              <b-form-input id="form-author-edit-input"
                            type="text"
                            v-model="editForm.author"
                            required
                            placeholder="Enter author">
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-read-edit-group">
              <b-form-checkbox-group v-model="editForm.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-button-group>
              <b-button type="submit" variant="primary">Update</b-button>
              <b-button type="reset" variant="danger">Cancel</b-button>
            </b-button-group>
          </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then((res) => {
          // this.message = 'Book added.';
          this.message = res.data.message; // alert user
          this.showMessage = true;
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      // wire up AJAX request
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then((res) => {
          this.message = res.data.message; // alert user
          this.showMessage = true; // alert user
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    editBook(book) {
      this.editForm = book;
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then((res) => {
          // this.message = 'Book removed.';
          this.message = res.data.message; // alert user
          this.showMessage = true;
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.id);
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide(); // closes the modal when the button is pressed.
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read,
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide(); // closes the modal when the button is pressed.
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide(); // closes the modal when the button is pressed.
      this.initForm();
      this.getBooks(); // why?
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide(); // closes the modal when the button is pressed.
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
