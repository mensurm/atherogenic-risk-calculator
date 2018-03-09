$( document ).ready(function() {
    $('.ui.form').form({
        fields: {
            total_cholesterol: {
                identifier: 'total_cholesterol',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Please enter total cholesterol value'
                    }
                ]
            },
            triglyceride: {
                identifier: 'triglyceride',
                rules: [
                    {
                        type: 'empty',
                        prompt: "Please enter triglyceride value"
                    }
                ]
            },
            high_density_lipoproteins: {
                identifier: 'high_density_lipoproteins',
                rules: [
                    {
                        type: 'empty',
                        prompt: "Please enter high desity lipoproteins value"
                    }
                ]
            }
        }
    });
});