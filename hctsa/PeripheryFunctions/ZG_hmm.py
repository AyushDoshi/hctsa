import math

import numpy

from hctsa.PeripheryFunctions import ZG_rdiv, ZG_rsum, ZG_rprod


def ZG_hmm(X, T='', K=2, cyc=100, tol=.0001):
    """
    Python Implementation currently slow used for loops same as orginal
    need to vectorize
    %
    % X - N x p data matrix
    % T - length of each sequence (N must evenly divide by T, default T=N)
    % K - number of states (default 2)
    % cyc - maximum number of cycles of Baum-Welch (default 100)
    % tol - termination tolerance (prop change in likelihood) (default 0.0001)
    %
    % Mu - mean vectors
    % Cov - output covariance matrix (full, tied across states)
    % P - state transition matrix
    % Pi - priors
    % LL - log likelihood curve
    %
    % Iterates until a proportional change < tol in the log likelihood
    % or cyc steps of Baum-Welch
    %
    % Machine Learning Toolbox
    % Version 1.0  01-Apr-96
    % Copyright (c) by Zoubin Ghahramani
    % http://mlg.eng.cam.ac.uk/zoubin/software.html
    %
    % ------------------------------------------------------------------------------
    % The MIT License (MIT)
    %
    % Copyright (c) 1996, Zoubin Ghahramani
    %
    % Permission is hereby granted, free of charge, to any person obtaining a copy
    % of this software and associated documentation files (the "Software"), to deal
    % in the Software without restriction, including without limitation the rights
    % to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    % copies of the Software, and to permit persons to whom the Software is
    % furnished to do so, subject to the following conditions:
    %
    % The above copyright notice and this permission notice shall be included in
    % all copies or substantial portions of the Software.
    %
    % THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    % IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    % FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    % AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    % LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    % OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    % THE SOFTWARE.
    % ------------------------------------------------------------------------------

    """

    # For my purpose X should always be Nx1

    N = len(X)
    p = 1
    if T == '':
        T = N

    if N % T != 0:
        return None

    N /= T

    Cov = numpy.cov(X)

    Mu = numpy.random.normal(0, 1, K) * math.sqrt(Cov) + numpy.ones(K) * numpy.mean(X)

    Pi = numpy.random.normal(0, 1, (1, K))
    Pi /= numpy.sum(Pi)

    P = numpy.random.uniform(0, 1, (K, K))
    P = ZG_rdiv(P, ZG_rsum(P))

    LL = []
    lik = 0

    alpha = numpy.zeros((T, K))
    beta = numpy.zeros((T, K))
    gamma = numpy.zeros((T, K))

    B = numpy.zeros((T, K))
    k1 = (2 * math.pi) ** (-p / 2)

    for cycle in range(cyc):

        Gamma = []
        Gammasum = numpy.zeros((1, K))
        Scale = numpy.zeros((T, 1))
        Xi = numpy.zeros((T - 1, K * K))

        for n in range(int(N)):

            # Assuming P = 1 makes Cov single value not matrix
            iCov = 1 / Cov

            k2 = k1 / numpy.sqrt(Cov)

            # get rid of for loops
            for i in range(T):

                for l in range(K):
                    d = Mu[l] - X[(n - 1) * T + i]

                    B[i, l] = k2 * numpy.exp(-.5 * d * iCov * d)

            scale = numpy.zeros((T, 1))
            alpha[0, :] = numpy.multiply(Pi, B[0, :])
            scale[0] = numpy.sum(alpha[0, :])
            alpha[0, :] = alpha[0, :] / scale[0]

            for i in range(1, T):
                alpha[i, :] = numpy.multiply(numpy.matmul(alpha[i - 1, :], P), B[i, :])
                scale[i] = numpy.sum(alpha[i, :])
                alpha[i, :] = alpha[i, :] / scale[i]

            beta[T - 1, :] = numpy.ones((1, K)) / scale[T - 1]

            for i in range(T - 2, -1, -1):
                beta[i, :] = numpy.matmul(numpy.multiply(beta[i + 1, :], B[i + 1, :]), P.T) / scale[i]

            gamma = numpy.multiply(alpha, beta)
            gamma = ZG_rdiv(gamma, ZG_rsum(gamma))
            gammasum = numpy.sum(gamma, axis=0)

            xi = numpy.zeros((T - 1, K * K))

            for i in range(T - 1):
                t = numpy.multiply(P, numpy.matmul(alpha[i, :].T, numpy.multiply(beta[i + 1, :], B[i + 1, :])))
                xi[i, :] = t.flatten('F') / numpy.sum(t)

            Scale = Scale + numpy.log(scale)

            if not Gamma:

                Gamma = gamma

            else:

                Gamma = numpy.vstack((Gamma, gamma))

            Gammasum += gammasum
            Xi += xi

        Mu = numpy.zeros((K, p))
        Mu = numpy.matmul(Gamma.T, X)

        Mu = ZG_rdiv(Mu, Gammasum.T)

        sxi = numpy.transpose(ZG_rsum(Xi.T))
        sxi = numpy.reshape(sxi, (K, K)).T

        P = ZG_rdiv(sxi, ZG_rsum(sxi))

        Pi = numpy.zeros((1, K))

        # can vectorize below
        for i in range(int(N)):
            Pi = Pi + Gamma[(i - 1) * T + 1, :]

        Pi /= N

        Cov = 0

        for l in range(K):
            d = X - Mu[l]
            Cov += numpy.matmul(ZG_rprod(d, Gamma[:, l]).T, d)

        Cov /= numpy.sum(Gammasum)

        oldlik = lik
        lik = numpy.sum(Scale)
        LL.append(lik)

        if cycle <= 1:

            likbase = lik


        elif lik < oldlik:

            print("Error old lik better")

        elif (lik - likbase) < (1 + tol) * (oldlik - likbase):
            break

    return Mu, Cov, P, Pi, LL
