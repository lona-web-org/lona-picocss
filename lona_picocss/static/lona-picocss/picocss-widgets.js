// based on https://github.com/picocss/pico/blob/45e4a588435ce5977e23a8f9034542d7a8d76922/docs/js/modal.js

class LonaPicocssModalWidget {
    constructor(lona_window) {
        this.lona_window = lona_window;

        this.openClass = 'modal-is-open';
        this.openingClass = 'modal-is-opening';
        this.closingClass = 'modal-is-closing';
        this.visibleClass = 'modal-is-visible';
        this.animationDuration = 400;
        this.scrollbarWidth = this.getScrollbarWidth();
    }

    getScrollbarWidth() {
        // Creating invisible container
        const outer = document.createElement('div');

        outer.style.visibility = 'hidden';
        outer.style.overflow = 'scroll'; // forcing scrollbar to appear
        outer.style.msOverflowStyle = 'scrollbar'; // needed for WinJS apps

        document.body.appendChild(outer);

        // Creating inner element and placing it in the container
        const inner = document.createElement('div');

        outer.appendChild(inner);

        // Calculating difference between container's full width and the
        // child width
        const scrollbarWidth = (outer.offsetWidth - inner.offsetWidth);

        // Removing temporary elements from the DOM
        outer.parentNode.removeChild(outer);

        return scrollbarWidth;
    }

    open() {
        const scrollbarIsVisible = document.body.scrollHeight > screen.height;

        if(scrollbarIsVisible) {
            document.documentElement.style.setProperty(
                '--scrollbar-width',
                `${this.scrollbarWidth}px`,
            );
        }

        document.documentElement.classList.add(
            this.openClass,
            this.openingClass,
        );

        setTimeout(() => {
            document.documentElement.classList.remove(this.openingClass);
            document.documentElement.classList.add(this.visibleClass);
        }, this.animationDuration);

        this.root_node.setAttribute('open', true);
    }

    close() {
        document.documentElement.classList.add(this.closingClass);

        setTimeout(() => {
            document.documentElement.classList.remove(
                this.closingClass,
                this.openClass,
                this.visibleClass,
            );

            document.documentElement.style.removeProperty('--scrollbar-width');
            this.root_node.removeAttribute('open');
        }, this.animationDuration);
    }

    updateOpenState(initial) {
        if(this.data['open']) {
            this.open();
        } else {
            if(initial) {
                return;
            }

            this.close();
        }
    }

    setup() {
        this.updateOpenState(true);
    }

    data_updated() {
        this.updateOpenState();
    }
}


Lona.register_widget_class('LonaPicocssModalWidget', LonaPicocssModalWidget);
