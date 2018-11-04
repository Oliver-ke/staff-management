

window.addEventListener('DOMContentLoaded', function () {
  var myDatepicker = document.querySelector('input[id="date"]');
  var myDatepicker2 = document.querySelector('input[id="date2"]');
  var myDatepicker3 = document.querySelector('input[id="date3"]');
      myDatepicker.DatePickerX.init({
        mondayFirst      : true,
        format           : 'yyyy-mm-dd',
        minDate          : new Date(0, 0),
        maxDate          : new Date(9999, 11, 31),
        weekDayLabels    : ['Mo', 'Tu', 'We', 'Th', 'Fr', 'St', 'Su'],
        shortMonthLabels : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        singleMonthLabels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        todayButton      : true,
        todayButtonLabel : 'Today',
        clearButton      : true,
        clearButtonLabel : 'Clear'
  });

  myDatepicker2.DatePickerX.init({
    mondayFirst      : true,
    format           : 'yyyy-mm-dd',
    minDate          : new Date(0, 0),
    maxDate          : new Date(9999, 11, 31),
    weekDayLabels    : ['Mo', 'Tu', 'We', 'Th', 'Fr', 'St', 'Su'],
    shortMonthLabels : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    singleMonthLabels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    todayButton      : true,
    todayButtonLabel : 'Today',
    clearButton      : true,
    clearButtonLabel : 'Clear'
  });
  
  myDatepicker3.DatePickerX.init({
    mondayFirst      : true,
    format           : 'yyyy-mm-dd',
    minDate          : new Date(0, 0),
    maxDate          : new Date(9999, 11, 31),
    weekDayLabels    : ['Mo', 'Tu', 'We', 'Th', 'Fr', 'St', 'Su'],
    shortMonthLabels : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    singleMonthLabels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    todayButton      : true,
    todayButtonLabel : 'Today',
    clearButton      : true,
    clearButtonLabel : 'Clear'
});
  });
    