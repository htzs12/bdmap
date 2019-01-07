function Data() {

}


Data.prototype.run = function () {
    var self = this;
    self.listenAddEvent();
};


Data.prototype.listenAddEvent = function () {
    var addBtn = $('.add');

};


$(function () {
    var add = new Data();
    add.run();
});