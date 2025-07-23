var rect = {
    width: 10,
    height: 20,
    draw: function() {
        console.log('Drawing rectangle', this.width, this.height);
    },
    calculateArea: function() {
        return this.width * this.height;
    },
    calculateRange: function() {
        return this.width + this.height;
    }
};
var message = rect.draw();
var area = rect.calculateArea();
var range = rect.calculateRange();

console.log(message);
console.log(area);
console.log(range);

