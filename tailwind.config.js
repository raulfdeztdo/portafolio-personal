/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./**/*.html', './**/*.py'],
    darkMode: 'class',
    theme: {
        extend: {
            backgroundImage: {
                '1': "url('/images/bg-1.svg')",
                '2': "url('/images/bg-2.svg')",
                '3': "url('/images/bg-3.svg')",
                '3b': "url('/images/bg-3b.svg')",
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}