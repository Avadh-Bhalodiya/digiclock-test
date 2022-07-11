$(document).ready(function () {
    $('.submitBnt').click(function(event){
        console.log('Button Clicked')

        var name = $('.name').val()
        var email = $('.email').val()
        var subject = $('.subject').val()
        var comments = $('.comments').val()
        var statusElm = $('.status')
        statusElm.empty()

        if(email.length > 5 && email.includes('@') && email.includes('.')){
            console.log('valid email')
        }
        else {
            event.preventDefault()
            console.log('Invalid email')
        }

        if(subject.length > 2)
        {
            console.log('valid subject')
        }
        else{
            event.preventDefault()
            console.log('Invalid subject')
        }

        if(comments.length >= 3)
        {
            console.log('valid comment')
        }
        else{
            event.preventDefault()
            console.log('Invalid comment')
        }
    })
})
